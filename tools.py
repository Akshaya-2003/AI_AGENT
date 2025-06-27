#tools.py
from langchain.tools import tool
import wikipedia
from duckduckgo_search import DDGS

@tool
def DuckDuckGo_Search(query: str) -> str:
    """Search the web using DuckDuckGo and return top 3 titles and snippets."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            results.append(r['body'])  # Only return the snippet
    return "\n".join(results) if results else "No recent news found."

@tool
def Wikipedia_Tool(query: str) -> str:
    """Search Wikipedia for a given query and return the summary."""
    try:
        return wikipedia.summary(query, sentences=5)
    except Exception as e:
        return f"Error fetching Wikipedia summary: {e}"

@tool
def Wikipedia_Image(query: str) -> str:
    """Get the first image from a Wikipedia page."""
    try:
        page = wikipedia.page(query)
        return page.images[0] if page.images else ""
    except Exception:
        return ""
