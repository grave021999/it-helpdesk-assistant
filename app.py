import streamlit as st
from src.a2a_layer.orchestrator import Orchestrator

orchestrator = Orchestrator()

st.set_page_config(page_title="IT Helpdesk Assistant 🤖", page_icon="💬", layout="centered")

st.title("💬 IT Helpdesk Assistant")
st.write("Ask any question about your IT tickets below.")

st.sidebar.header("🧭 Controls")
if st.sidebar.button("🆕 Start New Chat"):
    st.session_state.chat_history = []
    st.sidebar.success("Chat history cleared! Start fresh 👇")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.text_input("Enter your query:", placeholder="e.g. show weekly report or open tickets")

if st.button("Ask"):
    if user_query:
        with st.spinner("Thinking..."):
            response = orchestrator.process_query(user_query)
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("AI", response))
    else:
        st.warning("Please enter a query before asking.")

for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"🧑 **{speaker}:** {message}")
    else:
        st.markdown(f"🤖 **{speaker}:** {message}")
