class ExecutionHandler:
    def __init__(self, slippage=0.0, commission_per_trade=0.0):
        self.slippage = slippage
        self.commission = commission_per_trade

    def execute_order(self, signal, price):
        """
        Simulates trade execution with slippage and commission.
        
        Args:
            signal (int): +1 for buy, -1 for sell, 0 for no trade
            price (float): market price at signal time

        Returns:
            executed_price (float): adjusted price after slippage
            cost (float): transaction cost
        """
        executed_price = price * (1 + self.slippage * signal)
        cost = self.commission
        return executed_price, cost
