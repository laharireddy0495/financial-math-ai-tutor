from dotenv import load_dotenv
import os
import streamlit as st
from google import genai

load_dotenv()

# Read API key (Streamlit Cloud first, then local .env)
API_KEY = None

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=API_KEY)

TUTOR_SYSTEM_PROMPT = """
You are an expert and friendly Financial Mathematics Tutor.

Explain concepts step by step.
Use simple language.
Never reveal chain of thought.
Guide the student instead of immediately giving the final answer.
"""


def run_tutor_turn(chat_history):

    user_message = chat_history[-1]["content"] if chat_history else ""

    prompt = f"""
{TUTOR_SYSTEM_PROMPT}

Student:
{user_message}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite"
            contents=prompt,
        )

        return (
            response.text,
            "Gemini response generated successfully."
        )

    except Exception as e:

        st.error(f"Gemini Error:\n{e}")

        return (
            "Gemini request failed.",
            str(e)
        )
