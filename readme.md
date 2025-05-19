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

## 🐳 Docker & Development Setup

This project uses **Docker Compose** to manage two services:

- 🧠 `ollama` – runs the Mistral model locally via REST API  
- 💬 `app` – your Flask-based legal chatbot  

---

### 📦 Prerequisites

- Docker Desktop  
- Docker Compose (v2+)  
- Internet connection (first-time model pull only)  

---

### 🚀 Quick Start

```
docker-compose up --build
```

Then open: [http://localhost:5000](http://localhost:5000)

Ollama will auto-run the `mistral` model. The Flask app supports hot-reloading for fast dev cycles.

---

### 🔁 Fast Iteration (No Rebuilds Needed)

Thanks to volume mounting:

- Code & template changes (e.g., `chatbot.py`, `chat.html`, `legal_qa.csv`) auto-reload
- No rebuild or restart needed in most cases

To quickly restart just the app:

```
docker-compose restart app
```

---

### 🧠 Model Persistence

- The Mistral model is cached in a Docker volume (`ollama_models`)
- It is pulled once, even if you restart or rebuild
- Ollama won’t re-download it every time

---

### ⚙️ Key Dev Config Highlights

```yaml
volumes:
  - .:/app                   # Live-reload Flask code
command:
  flask run --host=0.0.0.0 --port=5000
```

---

### 💡 Common Commands

| Task                        | Command                          |
|-----------------------------|-----------------------------------|
| Start everything            | `docker-compose up --build`      |
| Restart only the app        | `docker-compose restart app`     |
| Stop all containers         | `docker-compose down`            |
| Rebuild just the Flask app  | `docker-compose build app`       |
| View logs                   | `docker-compose logs -f app`     |

---

For production: use a WSGI server like **Gunicorn** instead of the Flask dev server.

---

## 📄 License

MIT License © 2025

---

## 👨‍⚖️ Maintainer

**Basudev Singh** – *Supreme Court of Guyana* 🇬🇾  
*Master of Science in Information Technology*
