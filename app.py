#app.py
from fastapi import FastAPI, HTTPException, Request
from models import ResearchResponse
from main import run_research
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/research", response_model=ResearchResponse)
async def research(request: Request):
    body = await request.json()
    topic = body.get("topic")
    if not topic:
        raise HTTPException(status_code=400, detail="Missing topic")

    try:
        result = run_research(topic)
        return ResearchResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")
