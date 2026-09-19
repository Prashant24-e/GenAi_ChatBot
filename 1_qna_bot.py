from dotenv import load_dotenv
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Get API key from Streamlit Secrets or local .env
api_key = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

st.title("AskBuddy 🤖 AI QNA Bot")
st.markdown("My QNA bot with LangChain and Google Gemini!")


def extract_text(content):
    """Extract plain text from Google Generative AI response content."""

    if isinstance(content, str):
        return content

    elif isinstance(content, list):
        return "\n".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in content
        )

    return str(content)


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]

    st.chat_message(role).markdown(content)


# Chat input
query = st.chat_input("Ask Anything")

if query:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    st.chat_message("user").markdown(query)

    # Get response from Gemini
    response = llm.invoke(query)
    answer = extract_text(response.content)

    # Display AI response
    st.chat_message("assistant").markdown(answer)

    # Store AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )