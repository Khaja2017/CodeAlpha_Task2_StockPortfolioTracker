# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 320,
    "AMZN": 3500
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")

# User input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not found in price list.")

# Calculate investment
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock} - {quantity} shares × ${price} = ${value}")

print("\n💰 Total Investment Value: $", total_investment)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("📁 Portfolio saved to portfolio.txt")