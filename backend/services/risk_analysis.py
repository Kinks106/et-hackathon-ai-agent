import yfinance as yf
import numpy as np

def get_risk_assessment(stock: yf.Ticker) -> dict:
    try:
        history = stock.history(period="1y")
        info = stock.info
        returns = history['Close'].pct_change().dropna()
        volatility = returns.std() * np.sqrt(252)
        var_95 = np.percentile(returns, 5)
        max_drawdown = calculate_max_drawdown(history['Close'])
        skewness = returns.skew()
        kurtosis = returns.kurtosis()

        risk_assessment = {
            'Annualized Volatility': volatility,
            'Beta': info['beta'],
            'Value at Risk (95%)': var_95,
            'Maximum Drawdown': max_drawdown,
            'Sharpe Ratio': calculate_sharpe_ratio(returns),
            'Sortino Ratio': calculate_sortino_ratio(returns),
            'Rolling Volatility (30d)': returns.rolling(window=30).std().mean() * np.sqrt(252),
            'Skewness': skewness,
            'Kurtosis': kurtosis
        }
        return risk_assessment
    except Exception as e:
        print(e)
        return {"error": str(e)}
    
def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """
    Sharpe Ratio = (Mean Return - Risk Free Rate) / Std Dev of Returns
    """
    excess_returns = returns - (risk_free_rate / 252)
    sharpe_ratio = excess_returns.mean() / returns.std()
    return round(sharpe_ratio * np.sqrt(252), 2)

def calculate_max_drawdown(prices):
    cumulative_max = prices.cummax()
    drawdown = (prices - cumulative_max) / cumulative_max
    return round(drawdown.min(), 2)

def calculate_sortino_ratio(returns, risk_free_rate=0.02):
    downside_returns = returns[returns < 0]
    downside_std = downside_returns.std()
    if downside_std == 0:
        return 0
    excess_return = returns.mean() - (risk_free_rate / 252)
    sortino = excess_return / downside_std
    return round(sortino * np.sqrt(252), 2)