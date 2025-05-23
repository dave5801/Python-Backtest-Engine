from utils.data_loader import load_data
from strategies.moving_average import MovingAverageCrossStrategy
from engine.backtester import Backtester
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load historical price data
    try:
        data = load_data("data/sample_data.csv")
        print("Data loaded successfully.")
        print(data.head())
    except Exception as e:
        print("Failed to load data:", e)
        exit(1)

    # Initialize and configure strategy
    strategy = MovingAverageCrossStrategy(short_window=2, long_window=3)

    # Run backtest
    try:
        bt = Backtester(data, strategy)
        equity_curve = bt.run()
        print("Backtest completed.")
    except Exception as e:
        print("Backtest failed:", e)
        exit(1)

    # Plot equity curve
    try:
        if equity_curve:
            dates, values = zip(*equity_curve)
            plt.plot(dates, values, label="Equity Curve")
            plt.title("Portfolio Value Over Time")
            plt.xlabel("Date")
            plt.ylabel("Portfolio Value")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.savefig("equity_curve.png")
            plt.show()
        else:
            print("No trades were executed. Equity curve is empty.")
    except Exception as e:
        print("Failed to plot equity curve:", e)
