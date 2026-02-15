from pydantic import BaseModel
from typing import List,Optional


class NewsArticle(BaseModel):
    title: str  # Title or headline of the news article
    summary: str  # 2–3 line summary of the article
    url: Optional[str]  # Link to the full article
    sentiment: str  # One of: Positive, Negative, or Neutral
    key_points: List[str]  # Key takeaways or important events
    potential_impact: str  # Explanation of potential market/sector impact


class NewsSentimentAnalysis(BaseModel):
    articles: List[NewsArticle]  # List of analyzed articles
    verdict: str  # Overall sentiment-based interpretation or suggestion
    sentiment_score: float  # Numeric score from 0 to 10