# Stock Portfolio Tracker - CodeAlpha Internship

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 170,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")
print(stock_prices)
print()

num = int(input("Enter number of stocks you want to buy: "))

for i in range(num):

    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        portfolio[stock] = quantity

        investment = stock_prices[stock] * quantity

        total_investment += investment

        print("Added:", stock)
        print("Investment value:", investment)

    else:
        print("Stock not available!")

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():

    print(
        stock,
        "- Quantity:", quantity,
        "- Price:", stock_prices[stock],
        "- Value:", stock_prices[stock] * quantity
    )

print("\nTotal Investment Value = $", total_investment)


# Optional: Save to text file
file = open("portfolio.txt", "w")

file.write("STOCK PORTFOLIO SUMMARY\n")
file.write("-------------------------\n")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    file.write(
        f"{stock} | Quantity: {quantity} | Value: ${value}\n"
    )

file.write(f"\nTotal Investment = ${total_investment}")

file.close()

print("\nPortfolio saved to portfolio.txt")