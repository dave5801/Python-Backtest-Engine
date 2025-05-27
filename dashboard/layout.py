import pandas as pd
import plotly.graph_objs as go
from dash import html, dcc
from utils.metrics import compute_cagr, compute_max_drawdown, compute_sharpe_ratio

# Dummy load for now; replace with actual strategy and backtest result
from strategies.moving_average import MovingAverageCrossStrategy
from engine.backtester import Backtester
from utils.data_loader import load_data

def create_layout():
    # Load and run strategy
    data = load_data("data/sample_data.csv")  # <- Replace with your preferred asset
    strategy = MovingAverageCrossStrategy()
    bt = Backtester(data, strategy)
    equity_curve = bt.run()

    df = pd.DataFrame(equity_curve, columns=["date", "value"]).set_index("date")

    # Metrics
    cagr = compute_cagr(equity_curve)
    max_dd = compute_max_drawdown(equity_curve)
    sharpe = compute_sharpe_ratio(equity_curve)

    # Equity curve plot
    equity_fig = go.Figure()
    equity_fig.add_trace(go.Scatter(x=df.index, y=df["value"], name="Portfolio Value"))
    equity_fig.update_layout(title="Equity Curve", xaxis_title="Date", yaxis_title="Value")

    # Price plot
    data["short_ma"] = data["close"].rolling(3).mean()
    data["long_ma"] = data["close"].rolling(5).mean()

    price_fig = go.Figure()
    price_fig.add_trace(go.Scatter(x=data.index, y=data["close"], name="Close"))
    price_fig.add_trace(go.Scatter(x=data.index, y=data["short_ma"], name="Short MA"))
    price_fig.add_trace(go.Scatter(x=data.index, y=data["long_ma"], name="Long MA"))
    price_fig.update_layout(title="Price & Moving Averages", xaxis_title="Date", yaxis_title="Price")

    return html.Div([
        html.H1("Quant Backtest Dashboard"),
        html.Div([
            html.P(f"CAGR: {cagr:.2%}"),
            html.P(f"Max Drawdown: {max_dd:.2%}"),
            html.P(f"Sharpe Ratio: {sharpe:.2f}"),
        ], style={"padding": "10px", "fontSize": "18px"}),
        dcc.Graph(figure=price_fig),
        dcc.Graph(figure=equity_fig)
    ])

