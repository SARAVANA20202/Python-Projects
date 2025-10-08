# Display Remaining Stock for Each Fruit
inventory = {
    "apple": 50,
    "banana": 40,
    "orange": 30,
    "mango": 20
}

print("=== Remaining Stock for Each Fruit BEFORE Sales ===")
for fruit, qty in inventory.items():
    print(f"{fruit.title()}: {qty} left")
print("\n")

# List of orders (each order is a dict: fruit -> quantity)
orders = [
    {"apple": 5, "banana": 10},
    {"orange": 7, "mango": 3, "apple": 2},
    {"banana": 8, "apple": 3},
    {"mango": 5, "orange": 6},
    {"apple": 2, "banana": 4, "mango": 2}
]

# Prices for each fruit (for sales report)
prices = {
    "apple": 3,
    "banana": 2,
    "orange": 4,
    "mango": 5
}

# Process orders and update inventory
total_sales_report = []
print("=== Sales Orders ===")
for idx, order in enumerate(orders):
    order_total = 0
    print(f"Order {idx + 1}:")
    for fruit, qty in order.items():
        if inventory[fruit] >= qty:
            inventory[fruit] -= qty
            cost = prices[fruit] * qty
            order_total += cost
            print(f" - {fruit.title()} x {qty} @ ₹{prices[fruit]} each = ₹{cost}")
        else:
            print(f" - {fruit.title()} x {qty}: Only {inventory[fruit]} left. Skipping.")
    print(f"Order Total: ₹{order_total}\n")
    total_sales_report.append(order_total)

# Final Sales Fruits Report
print("=== Final Sales Fruits Report ===")
for idx, order in enumerate(orders):
    print(f"Order {idx + 1} Total: ₹{total_sales_report[idx]}")
print(f"Grand Total Sales: ₹{sum(total_sales_report)}\n")

# Display Remaining Stock after Sales
print("=== Remaining Stock for Each Fruit AFTER Sales ===")
for fruit, qty in inventory.items():
    print(f"{fruit.title()}: {qty} left")