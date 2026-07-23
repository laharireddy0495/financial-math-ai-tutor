import streamlit as st
from backend import run_tutor_turn

# Web Page config layout setting
st.set_page_config(page_title="AI Financial Tutor", layout="wide")
st.title("🧠 Financial Math Tutor (AI Mind Reader Dashboard)")

# Session state initialization setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "latest_thoughts" not in st.session_state:
    st.session_state.latest_thoughts = "Waiting for student to ask a question..."

# Page layout split mapping definitions
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("💬 Student Chat Interface")
    
    # Clean output tracking displays for older engine platforms
    for msg in st.session_state.messages:
        role_label = "🧑‍🎓 Student" if msg["role"] == "user" else "🤖 AI Tutor"
        st.markdown(f"**{role_label}:** {msg['content']}")
        st.markdown("---")

    # Native basic form component mapping preventing state submission drops
    with st.form(key="chat_input_form", clear_on_submit=True):
        user_query = st.text_input("Type your financial math question here:")
        submit_btn = st.form_submit_button(label="Send Message")

    if submit_btn and user_query.strip():
        # Save session message logs safely
        st.session_state.messages.append({"role": "user", "content": user_query.strip()})
        
        # AI processing pipeline loop parameters
        with st.spinner("AI is thinking..."):
            student_reply, system_thoughts = run_tutor_turn(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": student_reply})
            st.session_state.latest_thoughts = system_thoughts
        
        # Old stream version fallback controls mapping
        try:
            st.experimental_rerun()
        except AttributeError:
            pass

with right_col:
    st.subheader("🛡️ AI Reasoning Summary")
    st.info("This panel summarizes the AI tutor's reasoning and solution strategy before generating a response.")
    st.code(st.session_state.latest_thoughts, language="markdown")
