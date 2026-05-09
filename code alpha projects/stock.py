import csv

# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 300
}

portfolio = {}

def add_stock():
    while True:
        stock = input("Enter stock name (or 'done'): ").upper()
        
        if stock == "DONE":
            break
        
        if stock in stocks:
            qty = int(input(f"Enter quantity of {stock}: "))
            buy_price = float(input(f"Enter buying price of {stock}: "))
            
            portfolio[stock] = {
                "quantity": qty,
                "buy_price": buy_price,
                "current_price": stocks[stock]
            }
        else:
            print("⚠ Stock not available!")

def calculate_portfolio():
    total_investment = 0
    current_value = 0

    print("\n📊 Portfolio Summary:")
    print("-" * 40)

    for stock, data in portfolio.items():
        invested = data["quantity"] * data["buy_price"]
        current = data["quantity"] * data["current_price"]
        profit_loss = current - invested

        total_investment += invested
        current_value += current

        print(f"{stock}:")
        print(f"  Invested: {invested}")
        print(f"  Current Value: {current}")
        print(f"  Profit/Loss: {profit_loss}")
        print("-" * 40)

    total_profit = current_value - total_investment

    print(f"💰 Total Investment: {total_investment}")
    print(f"📈 Current Value: {current_value}")
    print(f"🔥 Total Profit/Loss: {total_profit}")

    return total_investment, current_value, total_profit

def save_to_csv():
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Buy Price", "Current Price"])

        for stock, data in portfolio.items():
            writer.writerow([
                stock,
                data["quantity"],
                data["buy_price"],
                data["current_price"]
            ])
    
    print("📁 Portfolio saved to portfolio.csv")

def main():
    print("📈 Advanced Stock Portfolio Tracker")
    add_stock()
    calculate_portfolio()
    save_to_csv()

main()