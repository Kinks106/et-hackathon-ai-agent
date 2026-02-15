from pydantic import BaseModel
from typing import List

class AnalysisSection(BaseModel):
    summary: str  # 4–5 lines summarizing insights
    key_points: List[str]  # 1–10 AI-derived takeaways
    ai_score: int  # AI-evaluated score (must be between 0 and 10)


class FinancialAnalysisReport(BaseModel):
    growth_analysis: AnalysisSection  # Trends, valuation, and return signals
    risk_analysis: AnalysisSection  # Volatility, drawdowns, and risk exposure
    verdict: str




