import yfinance as yf
import matplotlib.pyplot as plt

# User Input
stock_name = input("Enter Stock Symbol: ")

# Download Data
data = yf.download(
    stock_name,
    start="2024-01-01",
    end="2025-01-01"
)

# Show Data
print(data.head())

# Graph
plt.figure(figsize=(12,6))

plt.plot(data['Close'])

plt.title(f"{stock_name} Stock Analysis")
plt.xlabel("Date")
plt.ylabel("Price")

plt.grid(True)

plt.show()