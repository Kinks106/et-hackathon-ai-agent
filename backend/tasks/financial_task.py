from crewai import Task
from backend.schemas.financial_schema import FinancialAnalysisReport
from backend.agents.financial_agent import financial_analyst


financial_analysis_task = Task(
    description=(
        "Use the `financial_analysis_data` tool to get stock price history and technical indicators for {ticker}. "
        "Analyze the data to identify trends, key support/resistance levels, and volatility patterns.\n\n"

        "Provide a summary of:\n"
        "- Recent price action\n"
        "- Key technical indicators (RSI, MACD, Moving Averages)\n"
        "- Potential short-term price targets\n\n"

        "Conclude with a clear signal (Buy/Sell/Hold) based on the technical analysis."
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