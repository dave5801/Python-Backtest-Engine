import pandas as pd

class MovingAverageCrossStrategy:
    def __init__(self, short_window=3, long_window=5):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        signals = pd.DataFrame(index=data.index)
        signals["signal"] = 0

        # Calculate moving averages
        short_ma = data["close"].rolling(window=self.short_window, min_periods=1).mean()
        long_ma = data["close"].rolling(window=self.long_window, min_periods=1).mean()

        position = 0

        for i in range(1, len(data)):
            if short_ma.iloc[i] > long_ma.iloc[i] and position == 0:
                signals.iloc[i] = 1
                position = 1
            elif short_ma.iloc[i] < long_ma.iloc[i] and position == 1:
                signals.iloc[i] = -1
                position = 0

        return signals

