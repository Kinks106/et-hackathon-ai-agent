from crewai import Task
from app.schemas.outlook_schema import InvestorOutlook
from app.agents.outlook_agent import investor_outlook_agent

investor_outlook_task = Task(
    description=(
        "Using the provided insights from news sentiment and financial analysis, generate an investment outlook for the stock `{ticker}`.\n\n"
        "The output should include tailored guidance for three types of investors:\n"
        "1. **Short-Term (6–12 months)**: Based on recent price action, volatility, and market sentiment.\n"
        "2. **Mid-Term (1–3 years)**: Based on earnings trends, financial metrics, and market position.\n"
        "3. **Long-Term (3+ years)**: Based on long-term sustainability, financial health, and macro outlook.\n\n"

        "You must incorporate:\n"
        "- **Sentiment trends** from news/media sources\n"
        "- **Financial data** including balance sheet strength, risk ratios, stock performance metrics\n\n"

        "Finally, provide:\n"
        "- An **overall investment recommendation** as one of: `Strong Buy`, `Buy`, `Hold`, `Sell`, or `Strong Sell`\n"
        "- A short **rationale** explaining how both sentiment and financial data influenced your outlook"
    ),
    agent=investor_outlook_agent,
    inputs=["ticker"],
    expected_output=(
        "A structured `InvestorOutlook` object containing:\n"
        "- `short_term_outlook`\n"
        "- `mid_term_outlook`\n"
        "- `long_term_outlook`\n"
        "- `overall` (investment recommendation enum)\n"
        "- `rationale` (combined reasoning)"
    ),
    output_pydantic=InvestorOutlook
)
