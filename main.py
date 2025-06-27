#main.py
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_ollama import ChatOllama
from tools import DuckDuckGo_Search, Wikipedia_Tool, Wikipedia_Image
from datetime import datetime

llm = ChatOllama(model="llama3")

tools = [
    Tool(name="Wikipedia", func=Wikipedia_Tool, description="General summary"),
    Tool(name="DuckDuckGo", func=DuckDuckGo_Search, description="Recent info"),
    Tool(name="Wikipedia Image", func=Wikipedia_Image, description="Get image")
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

def run_research(query: str) -> dict:
    print("> Running research query...")

    intro_prompt = f"Give a short introduction about {query}."
    achievements_prompt = f"What are the main achievements of {query}?"
    news_prompt = f"What are the most recent news or updates about {query}?"
    image_prompt = f"{query}"

    intro = agent.invoke({"input": intro_prompt}).get("output", "")
    achievements = agent.invoke({"input": achievements_prompt}).get("output", "")
    news = agent.invoke({"input": news_prompt}).get("output", "")
    image_url = Wikipedia_Image.invoke(image_prompt)

    return {
        "topic": query,
        "introduction": intro,
        "achievements": achievements,
        "recent_news": news,
        "image_url": image_url,
        "timestamp": datetime.now().isoformat()
    }
