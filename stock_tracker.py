# Stock Portfolio Tracker

stock_prices = {"AAPL": 180, "TSLA": 250, "MSFT": 410, "GOOGL": 165, "AMZN": 185}

portfolio = {}

print("Stock Portfolio Tracker")
print("Available stocks:")
for name in stock_prices:
    print(name, ": $", stock_prices[name])

while True:
    stock = input("\nEnter stock name (type done to finish): ")
    stock = stock.upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        portfolio[stock] = qty
    else:
        print("Stock not found, try again")

total = 0
print("\nYour Portfolio:")
for stock in portfolio:
    price = stock_prices[stock]
    qty = portfolio[stock]
    value = price * qty
    total = total + value
    print(stock, "x", qty, "= $", value)

print("\nTotal Investment: $", total)

save = input("Do you want to save this to a file? (yes/no): ")
if save == "yes":
    f = open("portfolio.txt", "w")
    f.write("Stock Portfolio Summary\n")
    for stock in portfolio:
        price = stock_prices[stock]
        qty = portfolio[stock]
        value = price * qty
        f.write(stock + " x " + str(qty) + " = $" + str(value) + "\n")
    f.write("Total Investment: $" + str(total) + "\n")
    f.close()
    print("Saved to portfolio.txt")