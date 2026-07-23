# 🧠 AI Financial Math Tutor (Prompt Engineering Showcase)

A production-grade educational application built on top of **Prompt Engineering Foundations**. It implements an interactive financial math tutor that acts as a pedagogical guide rather than a generic answer generator.

## 🚀 Prompt Engineering Core Foundations Implemented

*   **Chain-of-Thought (CoT) Reasoning**: The system forces the LLM to calculate compounding interest steps inside hidden `<thinking>...</thinking>` XML tags before replying to the student.
*   **Persona & Behavioral Guardrails**: Implements strict instructional hierarchies to maintain an encouraging teacher persona and manage topic constraints.
*   **Fail-Safe Local Fallback Architecture**: Features a local fallback layer to handle network errors smoothly, ensuring consistent user experience.

## 🛠️ Tech Stack
*   **Frontend**: Streamlit Dashboard UI layout.
*   **Backend Orchestration**: Python 3.7+ stable architecture.
*   **Core AI Engine**: Google Gemini API Integration.
