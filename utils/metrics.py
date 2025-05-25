import numpy as np
import pandas as pd

def compute_cagr(equity_curve):
    df = pd.DataFrame(equity_curve, columns=["date", "value"])
    df.set_index("date", inplace=True)
    
    start_value = df["value"].iloc[0]
    end_value = df["value"].iloc[-1]
    n_days = (df.index[-1] - df.index[0]).days
    years = n_days / 365.25
    
    cagr = (end_value / start_value) ** (1 / years) - 1
    return cagr


def compute_max_drawdown(equity_curve):
    df = pd.DataFrame(equity_curve, columns=["date", "value"])
    df.set_index("date", inplace=True)
    
    running_max = df["value"].cummax()
    drawdown = (df["value"] - running_max) / running_max
    max_dd = drawdown.min()
    return max_dd


def compute_sharpe_ratio(equity_curve, risk_free_rate=0.0, periods_per_year=252):
    df = pd.DataFrame(equity_curve, columns=["date", "value"])
    df.set_index("date", inplace=True)
    
    df["returns"] = df["value"].pct_change().dropna()
    excess_returns = df["returns"] - (risk_free_rate / periods_per_year)
    
    mean_excess_return = excess_returns.mean()
    std_excess_return = excess_returns.std()
    
    sharpe = (mean_excess_return / std_excess_return) * np.sqrt(periods_per_year)
    return sharpe
