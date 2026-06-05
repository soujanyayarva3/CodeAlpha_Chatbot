
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0F172A;
}

.stApp {
    background-color: #0F172A;
}

h1, h2, h3, p {
    color: white;
}

.chat-card {
    background-color: #1E293B;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Knowledge Base
faq = {
    "what is ai": "Artificial Intelligence (AI) enables machines to simulate human intelligence and decision-making.",
    "what is machine learning": "Machine Learning is a branch of AI that learns patterns from data.",
    "what is deep learning": "Deep Learning uses neural networks with multiple layers to learn complex patterns.",
    "what is python": "Python is a versatile programming language widely used in AI and Data Science.",
    "what is nlp": "Natural Language Processing allows computers to understand and generate human language.",
    "what is computer vision": "Computer Vision enables machines to analyze and understand images and videos.",
    "what is data science": "Data Science combines statistics, programming, and domain expertise to extract insights from data.",
    "what is chatbot": "A chatbot is software that simulates human conversation.",
    "what is neural network": "A neural network is a computational model inspired by the human brain.",
    "what is tensorflow": "TensorFlow is an open-source machine learning framework developed by Google.",
    "what is pytorch": "PyTorch is a popular deep learning framework used for research and production.",
    "what is supervised learning": "Supervised learning trains models using labeled datasets.",
    "what is unsupervised learning": "Unsupervised learning finds patterns in unlabeled data.",
    "what is reinforcement learning": "Reinforcement learning trains agents through rewards and penalties.",
    "hello": "Hello! Welcome to the AI Knowledge Assistant.",
    "how are you": "I'm functioning perfectly and ready to assist you."
}

# Session State
if "current_chat" not in st.session_state:
    st.session_state.current_chat = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = None

# LEFT SIDEBAR
with st.sidebar:

    st.title("🤖 AI Assistant")

    if st.button("➕ New Chat", use_container_width=True):

        if st.session_state.current_chat:
            st.session_state.chat_history.append({
                "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "messages": st.session_state.current_chat.copy()
            })

        st.session_state.current_chat = []
        st.session_state.selected_chat = None
        st.rerun()

    search = st.text_input("🔍 Search Chats")

    st.markdown("---")
    st.subheader("📜 Chat History")

    for i, chat in enumerate(st.session_state.chat_history):

        title = chat["messages"][0]["content"][:25] if chat["messages"] else "Chat"

        if search.lower() in title.lower():

            col1, col2 = st.columns([4,1])

            with col1:
                if st.button(
                    f"{title}",
                    key=f"chat_{i}",
                    use_container_width=True
                ):
                    st.session_state.selected_chat = i
                    st.rerun()

            with col2:
                if st.button("🗑️", key=f"del_{i}"):
                    st.session_state.chat_history.pop(i)
                    st.rerun()

# MAIN CONTENT
left, center, right = st.columns([1,3,1])

with center:

    st.title("🤖 AI Knowledge Assistant")

    st.caption(
        "Ask questions about Artificial Intelligence, Machine Learning, Python, NLP, and Data Science."
    )

    st.markdown("### Popular Topics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("Artificial Intelligence")

    with c2:
        st.info("Machine Learning")

    with c3:
        st.info("Python")

    # Show Selected Chat
    display_chat = st.session_state.current_chat

    if st.session_state.selected_chat is not None:
        display_chat = st.session_state.chat_history[
            st.session_state.selected_chat
        ]["messages"]

    for msg in display_chat:

        avatar = "👤" if msg["role"] == "user" else "🤖"

        with st.chat_message(msg["role"], avatar=avatar):
            st.write(msg["content"])

    user_input = st.chat_input(
        "Ask your AI question..."
    )

    if user_input:

        st.session_state.current_chat.append({
            "role": "user",
            "content": user_input
        })

        response = faq.get(
            user_input.lower().strip(),
            "Sorry, I don't currently have information about that topic."
        )

        st.session_state.current_chat.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()

# RIGHT PANEL
with right:

    st.subheader("📊 Insights")

    total_chats = len(st.session_state.chat_history)

    total_messages = sum(
        len(chat["messages"])
        for chat in st.session_state.chat_history
    ) + len(st.session_state.current_chat)

    st.metric("Chats", total_chats)
    st.metric("Messages", total_messages)

    st.markdown("---")

    st.subheader("📚 Categories")

    st.success("Artificial Intelligence")
    st.success("Machine Learning")
    st.success("Deep Learning")
    st.success("Python")
    st.success("NLP")
    st.success("Computer Vision")
    st.success("Data Science")
