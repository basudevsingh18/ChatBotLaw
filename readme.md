# ⚖️ Legal Chatbot – Law Assistant Powered by LLMs

A conversational legal chatbot that uses semantic search and a local LLM (via Ollama) to provide easy-to-understand legal answers, with optional Creole translation. Powered by Flask, FAISS, SentenceTransformers, and Mistral.

---

## 📦 Features

- ✅ Ask legal questions and get contextual answers  
- 📚 Cites legal sources from a CSV knowledge base  
- 💬 Supports English, Creole, or both  
- 🔍 Semantic search using embeddings (MiniLM + FAISS)  
- 🧠 Local LLM inference via [Ollama](https://ollama.com/)  
- 🐳 Dockerized with `docker-compose`  

---

## 📁 Project Structure

```
chatbot_app/
├── app.py                # Flask app
├── chatbot.py            # Embedding + Ollama API logic
├── legal_qa.csv          # Local knowledge base
├── requirements.txt      # Python dependencies
├── Dockerfile            # Flask app Docker setup
├── docker-compose.yml    # Multi-service setup
├── templates/
│   └── chat.html         # Chat UI (Jinja2 + JS)
└── static/
    └── styles.css        # Optional CSS (or inline)
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/legal-chatbot.git
cd legal-chatbot
```

### 2. Run the App with Docker Compose

```bash
docker-compose up --build
```

This launches:
- `Flask` app on [http://localhost:5000](http://localhost:5000)
- `Ollama` model server on `localhost:11434`

---

### 3. Pull and Start the Model (Mistral)

Open another terminal and run:

```bash
docker exec -it legal-chatbot-ollama-1 ollama run mistral
```

Now the chatbot can generate responses using the Mistral LLM locally.

---

## 🧠 How It Works

1. The chatbot reads `legal_qa.csv` and generates vector embeddings using `sentence-transformers`.
2. Incoming user questions are compared using **FAISS** to find the closest legal topic.
3. A natural language prompt is constructed and passed to **Ollama’s REST API**.
4. The model (e.g., `mistral`) generates a response which is returned via Flask.
5. Optionally, responses are translated to **Guyanese Creole**.

---

## 🌍 Language Support

Choose your preferred language below the chat:
- 🇬🇧 English  
- 🏝️ Creole  
- 🌐 Both  

---

## 📜 Environment Variables

None required by default.

You can set these optionally in `docker-compose.yml`:

```yaml
environment:
  - FLASK_ENV=production
```

---

## ✅ Requirements (for manual setup)

If you're running locally without Docker:

```bash
pip install -r requirements.txt
```

---

## 🧹 Useful Commands

| Task                       | Command                                           |
|----------------------------|---------------------------------------------------|
| Build & start containers   | `docker-compose up --build`                      |
| Pull & run Mistral model   | `docker exec -it legal-chatbot-ollama-1 ollama run mistral` |
| Stop containers            | `docker-compose down`                            |

---

## 📄 License

MIT License © 2025

---

## 👨‍⚖️ Maintainer

**Basudev Singh** – *Supreme Court of Guyana* 🇬🇾  
*Master of Science in Information Technology*
