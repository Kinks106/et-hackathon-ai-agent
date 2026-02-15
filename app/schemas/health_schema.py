from pydantic import BaseModel
from typing import List

class HealthSection(BaseModel):
    summary: str  # 4–5 line narrative summarizing insights for this section
    key_points: List[str]  # 3–10 key takeaways
    ai_score: int  # AI-evaluated score (0 to 10)


class FinancialHealthReport(BaseModel):
    balance_sheet: HealthSection  # Short-term liquidity and obligations
    income_statement: HealthSection  # Margins, returns, profitability
    verdict: str  # Final investor recommendation or insight


