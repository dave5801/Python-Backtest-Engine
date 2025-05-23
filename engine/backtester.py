class Backtester:
    def __init__(self, data, strategy, initial_cash=100000):
        self.data = data
        self.strategy = strategy
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.position = 0
        self.equity_curve = []

    def run(self):
        signals = self.strategy.generate_signals(self.data)

        for date, row in signals.iterrows():
            price = self.data.loc[date, "close"]
            signal = row["signal"]

            if signal == 1 and self.cash > 0:
                self.position = self.cash / price
                self.cash = 0
                print(f"[{date.date()}] BUY at {price:.2f}")
            elif signal == -1 and self.position > 0:
                self.cash = self.position * price
                self.position = 0
                print(f"[{date.date()}] SELL at {price:.2f}")

            portfolio_value = self.cash + self.position * price
            self.equity_curve.append((date, portfolio_value))

        return self.equity_curve
