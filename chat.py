import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=API_KEY)

st.set_page_config(page_title="Chat Bot Assistant", layout="wide")

st.title("🐶 Pet recommendation")
st.subheader("Analyzes data and provides insights")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Enter readings or symptoms...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = chat_model.invoke(user_input)

    response_text = response.content if hasattr(response, "content") else str(response)

    st.session_state.messages.append({"role": "assistant", "content": response_text})

    with st.chat_message("assistant"):
        st.markdown(response_text)
