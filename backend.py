from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

# Load Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

TUTOR_SYSTEM_PROMPT = """
You are an expert and friendly Financial Mathematics Tutor.

Teach concepts step by step.

Do NOT reveal your internal reasoning or chain of thought.

Guide the student instead of immediately giving the final answer unless they explicitly ask for it.

End your response with a short question that keeps the student engaged whenever appropriate.
"""


def run_tutor_turn(chat_history):
    """Gemini Tutor with fallback"""

    user_message = chat_history[-1]["content"] if chat_history else ""

    prompt = f"""
{TUTOR_SYSTEM_PROMPT}

Student:
{user_message}
"""

    try:
        response = client.models.generate_content(
           model="gemini-flash-latest",
            contents=prompt,
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

        print("Gemini Error:", e)

        reasoning_summary = f"""
Gemini API unavailable.

Fallback strategy:
• Detect the student's financial mathematics problem.
• Provide a guided explanation.
• Continue tutoring locally.
""".strip()

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
