import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Jermaine's PA", page_icon="🤖")

st.title("Jermaine's Personal Study Assistant")
st.markdown("Hi, my name is Pelumi.\nHow can I help you, Boss?")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Accept input with enter key
user_input = st.chat_input("Message Oluwapelumi...")

if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response, _ = generate_response(user_input, st.session_state.chat_history)
    
    # Append assistant message
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Force rerun to show new messages immediately
    st.rerun()


# Display chat history (skip system prompts)
for msg in st.session_state.chat_history:
    if msg["role"] == "system":
        continue
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

