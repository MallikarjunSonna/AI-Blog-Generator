import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set API key
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Serve index.html directly
@app.get("/")
def serve_home():
    return FileResponse("frontend/index.html")

@app.post("/blogs")
async def create_blogs(request: Request):
    """Generate blog content using LangGraph."""
    data = await request.json()
    topic = data.get("topic", "")

    groqllm = GroqLLM()
    llm = groqllm.get_llm()
    graph_builder = GraphBuilder(llm)

    if topic:
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic": topic})

        blog_data = state.get("blog", {})
        title = blog_data.get("title", "Untitled Blog")
        content = blog_data.get("content", "No content generated.")

        return {
            "success": True,
            "title": title,
            "content": content
        }

    return {"success": False, "error": "Topic not provided."}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
