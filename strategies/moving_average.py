class MovingAverageCrossStrategy:
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        data = data.copy()
        data['short_ma'] = data['close'].rolling(self.short_window).mean()
        data['long_ma'] = data['close'].rolling(self.long_window).mean()
        data['signal'] = 0
        data['signal'][self.short_window:] = (
            data['short_ma'][self.short_window:] > data['long_ma'][self.short_window:]
        ).astype(int)
        data['position'] = data['signal'].diff()
        return data
