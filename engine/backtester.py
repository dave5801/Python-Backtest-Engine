from engine.portfolio import Portfolio

class Backtester:
    def __init__(self, data, strategy):
        self.data = strategy.generate_signals(data)
        self.portfolio = Portfolio()

    def run(self):
        for date, row in self.data.iterrows():
            price = row['close']
            signal = row.get('position', 0)
            if signal == 1:
                self.portfolio.update(date, 1, price)
            elif signal == -1:
                self.portfolio.update(date, -1, price)
        return self.portfolio.history
