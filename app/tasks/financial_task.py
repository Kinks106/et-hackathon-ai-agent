from crewai import Task
from app.schemas.financial_schema import FinancialAnalysisReport
from app.agents.financial_agent import financial_analyst


financial_analysis_task = Task(
    description=(
        "Use the `financial_analysis_data` tool **only once**, inputting only the stock {ticker} (e.g., 'AAPL') as a plain string. "
        "From the returned data, perform a focused analysis on:\n\n"
        "**1. Growth Analysis**:\n"
        "- Evaluate price trends, return potential, valuation ratios (like PE, PB), and performance signals.\n\n"
        "**2. Risk Analysis**:\n"
        "- Assess volatility, drawdowns, Sharpe ratio, beta, and sensitivity to market fluctuations.\n\n"
        "For each section, provide:\n"
        "- A 5-10 line summary of the analysis\n"
        "- Include 3 to 10 bullet-pointed insights drawn from the data"
        "- An `ai_score` from 0 to 10 reflecting confidence or strength in that dimension\n\n"
        "Return the result as a structured `FinancialAnalysisReport` object."

        "Finally, produce an overall insight or recommendation of 5-10 lines for investors based on the collective sentiment pattern."
    ),
    agent=financial_analyst,
    inputs=["ticker"],
    expected_output=(
        "A `FinancialAnalysisReport` containing:\n"
        "- `growth_analysis`: with `summary`, `key_points`, and `ai_score`\n"
        "- `risk_analysis`: with `summary`, `key_points`, and `ai_score`"
    ),
    output_pydantic=FinancialAnalysisReport
)