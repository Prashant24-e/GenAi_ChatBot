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

# now for to store the data that has been talked aboiut before we are gonna use st.session_state_messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# to show the displayued data we are be using for loop 

for messages in st.session_state.messages:
    role = messages["role"]
    content = messages["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask Anything")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(extract_text(res.content))
    st.session_state.messages.append({"role":"ai","content":extract_text(res.content)})


