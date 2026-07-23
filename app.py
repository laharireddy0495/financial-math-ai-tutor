import streamlit as st
from backend import run_tutor_turn

# Page properties layout definitions setup
st.set_page_config(page_title="AI Financial Tutor", layout="wide")
st.title("🧠 Financial Math Tutor (AI Mind Reader Dashboard)")

# Memory parameter structure checks matching operations properties mapping setup
if "messages" not in st.session_state:
    st.session_state.messages = []

if "latest_thoughts" not in st.session_state:
    st.session_state.latest_thoughts = "Waiting for student..."

# Segment view render logic splits pipeline columns execution
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("💬 Student Chat Interface")
    
    # Continuous output canvas frame setup container layer
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

    # Stream component dynamic interactive element layer interface view target
    user_query = st.chat_input("Ask a financial mathematics question...")

    if user_query:
        # Instant state visual render updates integration loops mapping trace processing
        st.session_state.messages.append({"role": "user", "content": user_query})
        with chat_container:
            with st.chat_message("user"):
                st.write(user_query)

        # Thread blocking wait visualization animation loader spinner
        with st.spinner("AI is thinking..."):
            student_reply, reasoning = run_tutor_turn(st.session_state.messages)

        # Assistant response generation content delivery tracking execution append
        st.session_state.messages.append({"role": "assistant", "content": student_reply})
        with chat_container:
            with st.chat_message("assistant"):
                st.write(student_reply)

        # Refresh dashboard metadata values panel layouts
        st.session_state.latest_thoughts = reasoning

with right_col:
    st.subheader("🛡️ AI Reasoning Summary")
    st.info(
        "This panel summarizes the tutor's strategy without exposing internal chain of thought."
    )
    # Thread component frame updates placeholder target block layer mapping setup
    thoughts_placeholder = st.empty()
    thoughts_placeholder.code(st.session_state.latest_thoughts)
