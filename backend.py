import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Local ga run chesthe .env file load avthundhi
# Streamlit Cloud lo unte direct Secrets configuration automatic pickup avthundhi
if os.path.exists(".env"):
    load_dotenv()

# System secrets integration token setup check
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing! Check your .env file or Streamlit Secrets configuration.")

# Initialize the correct client using explicit authorization key mapping
client = genai.Client(api_key=api_key)

TUTOR_SYSTEM_PROMPT = """
You are an expert and friendly Financial Mathematics Tutor.
Teach concepts step by step.
Do NOT reveal your internal reasoning or chain of thought.
Guide the student instead of immediately giving the final answer unless they explicitly ask for it.
End your response with a short question that keeps the student engaged whenever appropriate.
"""

def run_tutor_turn(chat_history):
    """Gemini Tutor with structural multi-turn context and fallback"""
    
    # Reasoning window visualization parameter mapping extraction
    user_message = chat_history[-1]["content"] if chat_history else ""

    try:
        # Convert app memory loop schema into standard multi-turn types content lists
        formatted_contents = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            formatted_contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["content"])]
                )
            )

        # Apply standard dynamic configuration parameters rules mapping logic
        config = types.GenerateContentConfig(
            system_instruction=TUTOR_SYSTEM_PROMPT,
            temperature=0.7
        )

        # Modern unified model structure generation tracking execution target mapping
        response = client.models.generate_content(
             model="gemini-3.1-flash-lite", 
            contents=formatted_contents,
            config=config
        )

        student_text = response.text.strip()

        reasoning_summary = f"""
User Goal:
Understand or solve:
"{user_message}"

Tutor Strategy:
• Identify the financial mathematics topic.
• Explain the concept step by step.
• Avoid giving the complete solution immediately.
• Encourage the student with a guiding question.
""".strip()

    except Exception as e:
        # Streamlit terminal analytics server engine tracking systems trace pipeline
        print("Gemini SDK Execution Exception Trace:", e)

        reasoning_summary = f"""
Gemini API unavailable (Fallback active).
Error Details: {str(e)}

Fallback strategy:
• Detect the student's financial mathematics problem.
• Provide a guided explanation.
• Continue tutoring locally.
""".strip()

        # Hardcoded structural local backup triggers match checks
        if "1000" in user_message or "10%" in user_message:
            student_text = """
Let's solve it together.
This is a compound interest problem.
Instead of calculating everything immediately, can you remember the Future Value formula?
If not, I can give you a hint.
""".strip()
        else:
            student_text = """
I'm here to help!
Please tell me:
• Principal amount
• Interest rate
• Time period
We'll solve it step by step.
""".strip()

    return student_text, reasoning_summary
