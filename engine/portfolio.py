class Portfolio:
    def __init__(self, initial_cash=100000):
        self.cash = initial_cash
        self.position = 0
        self.history = []

    def update(self, date, signal, price):
        if signal == 1:  # Buy
            self.position = self.cash // price
            self.cash -= self.position * price
        elif signal == -1:  # Sell
            self.cash += self.position * price
            self.position = 0
        total_value = self.cash + self.position * price
        self.history.append((date, total_value))
