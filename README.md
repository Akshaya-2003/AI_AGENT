Here’s a complete `README.md` you can use for your GitHub repository:

---

# 🧠 Research Assistant API

This project is a FastAPI-based backend for conducting topic-based research using powerful tools like Wikipedia, DuckDuckGo, and image extraction—all orchestrated with LangChain and LLaMA 3 via Ollama.

## 🚀 Features

* Accepts a research topic and returns:

  * Short introduction
  * Major achievements
  * Recent news or updates
  * First Wikipedia image (if available)
* Integrates with:

  * 🦙 LLaMA 3 via `langchain_ollama`
  * 🌐 DuckDuckGo for current info
  * 📚 Wikipedia for summaries and images
* CORS enabled for frontend integration (e.g., React on `localhost:3000`)

---

## 🧩 Tech Stack

* **FastAPI** - Web server
* **LangChain** - Agent orchestration
* **Ollama + LLaMA 3** - LLM processing
* **Wikipedia** - Summary + images
* **DuckDuckGo** - Latest search results
* **Pydantic** - Response model validation

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/research-assistant-api.git
cd research-assistant-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, here’s a sample:

```
fastapi
uvicorn
wikipedia
duckduckgo-search
langchain
langchain-community
langchain-ollama
```

### 4. Start Ollama and Pull LLaMA 3

Make sure you have [Ollama](https://ollama.com) installed and running.

```bash
ollama pull llama3
```

---

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

The server will run at: `http://127.0.0.1:8000`

---

## 🧪 API Endpoint

### `POST /api/research`

**Request body (JSON):**

```json
{
  "topic": "Albert Einstein"
}
```

**Successful response:**

```json
{
  "topic": "Albert Einstein",
  "introduction": "Albert Einstein was a theoretical physicist...",
  "achievements": "He developed the theory of relativity...",
  "recent_news": "No recent news found.",
  "image_url": "https://upload.wikimedia.org/...",
  "timestamp": "2025-06-27T12:00:00"
}
```

---

## 📁 Project Structure

```
.
├── app.py              # FastAPI app entry point
├── main.py             # Core agent logic
├── models.py           # Pydantic response models
├── tools.py            # LangChain tools for research
└── README.md           # Project documentation
```

---

## 💡 Future Improvements

* Add caching for repeated queries
* Support PDF export of research results
* Add more image search tools (e.g., Bing API)
* Extend multi-language support

---

## 📜 License

Feel free to use and modify.

---