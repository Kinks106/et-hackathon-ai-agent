from pydantic import BaseModel
from typing import List
from enum import Enum

class Recommendation(str, Enum):
    STRONG_BUY = "Strong Buy"
    BUY = "Buy"
    HOLD = "Hold"
    SELL = "Sell"
    STRONG_SELL = "Strong Sell"


class InvestorOutlook(BaseModel):
    short_term_outlook: str  # 6–12 months suggestion based on trends/sentiment
    mid_term_outlook: str  # 1–3 years recommendation based on financial indicators
    long_term_outlook: str  # 3+ years advice based on health and sustainability
    overall: Recommendation  # Final recommendation: Strong Buy to Strong Sell
    rationale: str  # Justification combining news sentiment and financial signals



