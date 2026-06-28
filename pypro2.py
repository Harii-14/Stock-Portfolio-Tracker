stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = {}

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock = input("\nEnter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        value = stock_prices[stock] * quantity
        total_investment += value

        portfolio[stock] = {
            "quantity": quantity,
            "value": value
        }
    else:
        print("Stock not found!")

print("\n----- Portfolio Summary -----")
for stock, details in portfolio.items():
    print(f"{stock}: Quantity = {details['quantity']}, Value = ${details['value']}")

print(f"\nTotal Investment Value = ${total_investment}")

with open("stock_report.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock}: Quantity = {details['quantity']}, Value = ${details['value']}\n"
        )

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nReport saved as 'stock_report.txt'")

 