from pydantic import BaseModel

class ResearchResponse(BaseModel):
    topic: str
    introduction: str
    achievements: str
    recent_news: str
    image_url: str
    timestamp: str
