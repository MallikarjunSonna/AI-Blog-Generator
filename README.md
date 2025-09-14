---
title: AI Blog Generator
emoji: 📝
colorFrom: indigo
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
---

# AI Blog Generator (LangGraph + LangChain + FastAPI)

This project demonstrates how to build an **agentic AI system** for blog generation using **LangGraph** and **LangChain**, with a modular backend architecture.  
It generates structured blog posts (title + content) from a user-provided topic and serves them via a FastAPI-powered REST API.

---

## 🚀 Features
- **LangGraph for Agentic Workflows**: Encodes blog generation as a state graph.
- **LangChain Integration**: Orchestrates LLM calls (Groq Llama-3.1) for structured output.
- **Backend with FastAPI**: `/blogs` endpoint handles topic requests and returns generated blog posts.
- **Frontend (HTML + JS)**: Simple UI to enter topics and display blogs.
- **Dockerized Deployment**: Packaged and deployed as a Hugging Face Space.

---

## 🛠️ Tech Stack
- **LangGraph** – Agentic workflow engine  
- **LangChain** – LLM orchestration  
- **Groq API** – Llama-3.1 backend LLM  
- **FastAPI** – Backend REST service  
- **HTML + JS** – Lightweight frontend  
- **Docker + Hugging Face Spaces** – Deployment  

---

## 📂 Project Structure
```
ai-blog-generator/
├─ app.py              # FastAPI backend
├─ frontend/index.html # Frontend UI
└─ src/
   ├─ graphs/graph_builder.py   # Defines LangGraph workflow
   ├─ llms/groqllm.py           # LLM wrapper for Groq
   ├─ nodes/blog_node.py        # Nodes for title & content generation
   └─ states/blogstate.py       # State definitions (TypedDict + Pydantic)
```

---

## ⚡ How it Works
1. User enters a **topic** in the frontend.
2. FastAPI endpoint `/blogs` passes the topic to the **LangGraph workflow**.
3. **BlogNode** agents generate:
   - Blog Title
   - Blog Content
4. Response is sent back to the frontend and rendered in Markdown.

---

## 📖 Example
```json
POST /blogs
{ "topic": "AI in Healthcare" }
```

Response:
```json
{
  "success": true,
  "blog": {
    "title": "Transforming Healthcare with AI",
    "content": "Artificial Intelligence is revolutionizing healthcare..."
  }
}
```

---

## 🏗️ Deployment
This project is deployed on **Hugging Face Spaces**:  
👉 [Live Demo](https://huggingface.co/spaces/MallikarjunSonna/ai-blog-generator)
