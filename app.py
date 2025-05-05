import streamlit as st
from assistant.query_router import route_query
from assistant.chat_history import ChatHistory

st.set_page_config(page_title="Smart Workplace Assistant", layout="wide")

# Load chatbot image
st.markdown(
    """
    <style>
    .bot-img {
        width: 100px;
        margin-right: 15px;
        vertical-align: middle;
    }
    .chat-box {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .user-msg {
        font-weight: bold;
        color: #3e3e3e;
    }
    .bot-msg {
        color: #2c2c2c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Assistant Options")
st.sidebar.info("Ask about your tasks, progress, focus sessions, etc.")

# Chat Title
st.title("🤖 Smart Workplace Assistant")

# Chatbot image and input

st.subheader("Ask me anything about your productivity!")

# Chat history manager
chat_history = ChatHistory()
for q, a in chat_history.get_history():
    st.markdown(f"<div class='chat-box user-msg'>🧑‍💻 {q}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-box bot-msg'>🤖 {a}</div>", unsafe_allow_html=True)

# User input
query = st.text_input("Your question", placeholder="E.g., What are my top priorities today?")
if st.button("Ask") and query:
    answer = route_query(query)
    chat_history.add_to_history(query, answer)
    st.experimental_rerun()
