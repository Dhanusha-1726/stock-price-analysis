import yfinance as yf
import matplotlib.pyplot as plt

# Stock name
stock_name = "AAPL"

# Download stock data
data = yf.download(
    stock_name,
    start="2024-01-01",
    end="2025-01-01"
)

# Show first 5 rows
print(data.head())

# Plot closing price
plt.figure(figsize=(10,5))

plt.plot(data['Close'])

plt.title("Apple Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")

plt.grid(True)

plt.show()


# --------------------------------
# MULTIPLE STOCK COMPARISON
# --------------------------------

apple = yf.download(
    "AAPL",
    start="2024-01-01",
    end="2025-01-01"
)

tesla = yf.download(
    "TSLA",
    start="2024-01-01",
    end="2025-01-01"
)

plt.figure(figsize=(12,6))

plt.plot(apple['Close'], label='Apple')
plt.plot(tesla['Close'], label='Tesla')

plt.title("Apple vs Tesla Stock Comparison")

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.show()



import numpy as np

# Moving Averages
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Buy/Sell Signal
data['Signal'] = np.where(
    data['MA20'] > data['MA50'],
    1,
    0
)

# Trend Graph
plt.figure(figsize=(14,7))

plt.plot(data['Close'], label='Closing Price')
plt.plot(data['MA20'], label='20 Day MA')
plt.plot(data['MA50'], label='50 Day MA')

plt.title("AI Stock Trend Analysis")

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.show()

# Final Signal
latest_signal = data['Signal'].iloc[-1]

if latest_signal == 1:
    print("📈 BUY Signal Detected")
else:
    print("📉 SELL Signal Detected")