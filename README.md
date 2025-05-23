# Python-Backtest-Engine

A modular Python backtesting engine for systematic trading strategies. This project allows you to simulate and evaluate trading strategies on historical market data with realistic portfolio and execution constraints.

## 🚀 Features

- ✅ Pluggable strategy system (e.g., moving average crossover)
- ✅ Event-driven portfolio and trade simulation
- ✅ Realistic order execution modeling (basic for now)
- ✅ Performance tracking and equity curve visualization
- ✅ Clean, extensible architecture for future development

## 🗂️ Project Structure

```
quant_backtester/
│
├── data/                  # Historical price data (CSV)
├── strategies/            # Strategy logic (e.g., moving average)
├── engine/                # Core backtesting logic (portfolio, execution)
├── utils/                 # Helper modules (data loading, metrics)
├── main.py                # Entrypoint to run the backtest
├── config.json            # Strategy and engine parameters (optional)
└── requirements.txt       # Python dependencies
```

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/your-username/quant_backtester.git
cd quant_backtester
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Prepare your data:
   - Place your CSV file with columns like `date,open,high,low,close,volume` in the `data/` folder.

## 🧠 Example Strategy: Moving Average Crossover

The included strategy buys when the short-term moving average crosses above the long-term average, and sells when it crosses below.

To run the example:
```bash
python main.py
```

The script will:
- Load sample historical price data
- Run the backtest using the moving average strategy
- Plot the resulting equity curve

## 📈 Sample Output

*Equity Curve Plot*

Portfolio value over time

*(Future enhancement: trade log, drawdown chart, metrics report)*

## 🔧 Future Enhancements

- Transaction cost modeling (slippage, commission)
- Multi-asset and multi-strategy support
- Walk-forward and cross-validation testing
- Integration with ML-based signal generation
- Web dashboard via Streamlit or Flask

## 🤝 Contributing

Contributions are welcome! Ideas include:
- New strategies
- Additional metrics
- Improved backtest speed or accuracy
- Data loader integrations

## 📜 License

MIT License. Use freely with attribution.