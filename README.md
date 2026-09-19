# AskBuddy 🤖 — GenAI Q&A Chatbot

AskBuddy is a simple AI-powered Q&A chatbot built using **Python, Streamlit, LangChain, and Google Gemini**.

The application provides an interactive chat interface where users can ask questions and receive AI-generated responses while maintaining conversation history during the current session.

## 🚀 Live Demo

🔗 (https://chatbot-genai-g.streamlit.app/)

## ✨ Features

* 🤖 AI-powered question answering
* 💬 Interactive chat interface
* 🧠 Conversation history using Streamlit Session State
* 🔗 LangChain integration
* ✨ Google Gemini integration
* 🔐 Secure API key management
* ⚡ Lightweight Streamlit application

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini**
* **python-dotenv**
* **Git & GitHub**

## 📂 Project Structure

```text
genai-chatbot/
│
├── 1_qna_bot.py       # Main Streamlit application
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variable template
├── .gitignore         # Files excluded from Git
└── README.md          # Project documentation
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Prashant24-e/genai-chatbot.git
cd genai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Do not commit the `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run 1_qna_bot.py
```

The application will then be available locally through the Streamlit development server.

## 🔐 API Key Security

This project requires a Google Gemini API key.

The API key should never be hard-coded into the source code or uploaded to GitHub.

For local development, the key is stored in:

```text
.env
```

For Streamlit Cloud deployment, the key is stored using Streamlit Secrets.

The `.gitignore` file prevents sensitive environment files from being committed.

## 🧠 How It Works

The application follows a simple workflow:

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
User Query
  │
  ▼
LangChain
  │
  ▼
Google Gemini
  │
  ▼
AI Response
  │
  ▼
Streamlit Chat Interface
```

Conversation messages are stored using Streamlit's `session_state`, allowing the current conversation to remain visible while the user interacts with the application.

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

Deployment configuration:

```text
Repository: Prashant24-e/genai-chatbot
Branch: main
Main file: 1_qna_bot.py
```

The Google Gemini API key should be added through Streamlit's Secrets management rather than committed to the repository.

## 🔮 Future Improvements

Potential improvements include:

* Streaming responses
* Clear chat functionality
* Multiple conversation sessions
* Persistent chat history
* Improved error handling
* Model selection
* Temperature controls
* File-based Q&A
* Retrieval-Augmented Generation (RAG)
* Conversation export

## 👨‍💻 Author

**Prashant Chauhan**

GitHub: https://github.com/Prashant24-e

## 📄 License

This project is created for learning and educational purposes.
