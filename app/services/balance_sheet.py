import yfinance as yf
import numpy as np

def analyze_balance_sheet(stock: yf.Ticker) -> dict:
    """
    Analyzes a company's balance sheet using yfinance data, returning detailed financial health metrics.

    Parameters:
    - stock: yfinance Ticker object for the company.

    Returns:
    - dict: Detailed balance sheet analysis including metrics, ratios, trends, and health summary.
    """
    try:
        # Fetch balance sheet data
        df = stock.balance_sheet
        if df.empty or df.columns.empty:
            return {"error": "Balance sheet data is empty or unavailable.", "module": "balance_sheet_analysis"}

        # Get years from column timestamps
        years = sorted([str(col.year) for col in df.columns], reverse=True)[:3]
        if not years:
            return {"error": "No valid years found in balance sheet data.", "module": "balance_sheet_analysis"}

        # Initialize output dictionary
        analysis = {
            "Metrics": {},
            "Ratios": {},
            "Trends": {},
        }

        # Define key balance sheet items to extract
        balance_sheet_items = [
            "Total Assets",
            "Total Liabilities Net Minority Interest",
            "Common Stock Equity",
            "Long Term Debt",
            "Total Debt",
            "Cash And Cash Equivalents",
            "Current Debt",
        ]

        # Map years to actual column timestamps
        year_to_timestamp = {str(col.year): col for col in df.columns}

        # Extract metrics for each year
        for year in years:
            metrics = {}
            timestamp = year_to_timestamp.get(year)
            if not timestamp:
                metrics = {item: None for item in balance_sheet_items}
            else:
                for item in balance_sheet_items:
                    if item in df.index:
                        try:
                            value = float(df.loc[item, timestamp])
                            metrics[item] = value if not np.isnan(value) else None
                        except (KeyError, ValueError):
                            metrics[item] = None
                    else:
                        metrics[item] = None

            # Store metrics
            analysis["Metrics"][year] = metrics

            # Calculate ratios
            ratios = {}
            try:
                # Liquidity Ratios
                if metrics.get("Cash And Cash Equivalents") is not None and metrics.get("Current Debt") is not None:
                    ratios["Current Ratio"] = (
                        (metrics["Cash And Cash Equivalents"] + (metrics.get("Accounts Receivable") or 0)) /
                        metrics["Current Debt"] if metrics["Current Debt"] != 0 else np.nan
                    )
                    ratios["Current Ratio"] = round(ratios["Current Ratio"], 2) if not np.isnan(ratios["Current Ratio"]) else None

                # Solvency Ratios
                if metrics.get("Total Debt") is not None and metrics.get("Total Assets") is not None:
                    ratios["Debt to Assets"] = (
                        metrics["Total Debt"] / metrics["Total Assets"] if metrics["Total Assets"] != 0 else np.nan
                    )
                    ratios["Debt to Assets"] = round(ratios["Debt to Assets"], 2) if not np.isnan(ratios["Debt to Assets"]) else None

                if metrics.get("Total Debt") is not None and metrics.get("Common Stock Equity") is not None:
                    ratios["Debt to Equity"] = (
                        metrics["Total Debt"] / metrics["Common Stock Equity"] if metrics["Common Stock Equity"] != 0 else np.nan
                    )
                    ratios["Debt to Equity"] = round(ratios["Debt to Equity"], 2) if not np.isnan(ratios["Debt to Equity"]) else None

                # Capital Structure
                if metrics.get("Common Stock Equity") is not None and metrics.get("Total Assets") is not None:
                    ratios["Equity Ratio"] = (
                        metrics["Common Stock Equity"] / metrics["Total Assets"] if metrics["Total Assets"] != 0 else np.nan
                    )
                    ratios["Equity Ratio"] = round(ratios["Equity Ratio"], 2) if not np.isnan(ratios["Equity Ratio"]) else None


            except ZeroDivisionError:
                ratios.update({
                    "Current Ratio": None,
                    "Debt to Assets": None,
                    "Debt to Equity": None,
                    "Equity Ratio": None,
                })

            analysis["Ratios"][year] = ratios

        # Convert dictionary keys to strings for JSON compatibility
        def convert_keys_to_str(d):
            if isinstance(d, dict):
                return {str(k): convert_keys_to_str(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [convert_keys_to_str(item) for item in d]
            else:
                return d

        return convert_keys_to_str(analysis)

    except Exception as e:
        return {"error": f"[Balance Sheet Analysis] {str(e)}", "module": "balance_sheet_analysis"}
