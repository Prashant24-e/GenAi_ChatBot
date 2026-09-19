from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
import streamlit as st

st.title("AskBuddy 🤖 AI QNA Bot")
st.markdown("My QNA bot with langchain and google gemini !")


def extract_text(content):
    """Extracts plain text from Google Generative AI response content."""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        return "\n".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in content
        )
    else:
        return str(content)


query = st.chat_input("Ask Anything")
if query:
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(extract_text(res.content))

# while True:
#     query = input("User: ")

#     if query in ["exit","quit","close"]:
#         print("gooodbye!!")
#         break
#     res = llm.invoke(query)
#     print("Ai:",res.content.text)


