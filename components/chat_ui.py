import streamlit as st

def render_chat_bubble(role: str, content: str):
    with st.chat_message(role):
        st.write(content)

