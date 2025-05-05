import streamlit as st

class ChatHistory:
    def __init__(self):
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

    def add_to_history(self, user_msg, bot_msg):
        st.session_state.chat_history.append((user_msg, bot_msg))

    def get_history(self):
        return st.session_state.chat_history

    def clear(self):
        st.session_state.chat_history = []
