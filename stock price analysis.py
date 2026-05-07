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