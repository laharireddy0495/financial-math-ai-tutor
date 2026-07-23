import streamlit as st
from backend import run_tutor_turn

st.set_page_config(page_title="AI Financial Tutor", layout="wide")
st.title("🧠 Financial Math Tutor (AI Mind Reader Dashboard)")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "latest_thoughts" not in st.session_state:
    st.session_state.latest_thoughts = "Waiting for student..."

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("💬 Student Chat Interface")

    # Chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    # Input
    user_query = st.chat_input("Ask a financial mathematics question...")

    if user_query:
        st.session_state.messages.append(
            {"role": "user", "content": user_query}
        )

        with st.spinner("AI is thinking..."):
            student_reply, reasoning = run_tutor_turn(
                st.session_state.messages
            )

        st.session_state.messages.append(
            {"role": "assistant", "content": student_reply}
        )

        st.session_state.latest_thoughts = reasoning

        st.rerun()

with right_col:
    st.subheader("🛡️ AI Reasoning Summary")
    st.info(
        "This panel summarizes the tutor's strategy without exposing internal chain of thought."
    )
    st.code(st.session_state.latest_thoughts)
