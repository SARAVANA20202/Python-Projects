# Inventory_small_app.py

# Initial stock (vegetable name -> quantity)
inventory = {
    "tomato": 50,
    "potato": 100,
    "onion": 80,
    "carrot": 40,
    "cabbage": 30
}

# Prices of vegetables (per unit)
prices = {
    "tomato": 10,
    "potato": 20,
    "onion": 15,
    "carrot": 12,
    "cabbage": 25
}

# List to store all orders
orders = []


def take_order(customer_name, items):
    """
    items -> dictionary of vegetable: quantity
    Example: {"tomato": 5, "onion": 3}
    """
    total = 0
    order_details = {"customer": customer_name, "items": {}, "total": 0}

    for veg, qty in items.items():
        if veg in inventory and inventory[veg] >= qty:
            cost = prices[veg] * qty
            inventory[veg] -= qty  # reduce stock
            total += cost
            order_details["items"][veg] = {"qty": qty, "cost": cost}
        else:
            print(f"⚠ Not enough stock for {veg} (requested {qty}, available {inventory.get(veg, 0)})")

    order_details["total"] = total
    orders.append(order_details)
    print(f"✅ Order placed for {customer_name}. Total: ₹{total}\n")


def show_sales_report():
    print("\n===== FINAL SALES REPORT =====")
    grand_total = 0
    for order in orders:
        print(f"\nCustomer: {order['customer']}")
        for veg, details in order["items"].items():
            print(f"  {veg} - {details['qty']} x ₹{prices[veg]} = ₹{details['cost']}")
        print(f" Order Total = ₹{order['total']}")
        grand_total += order["total"]
    print("\n------------------------------")
    print(f"Grand Total Sales = ₹{grand_total}")
    print("------------------------------")


def show_remaining_stock():
    print("\n===== REMAINING STOCK =====")
    for veg, qty in inventory.items():
        print(f"{veg}: {qty} left")


# ---------------------------
# Example Run
# ---------------------------

# Taking orders
take_order("Saravana", {"tomato": 5, "onion": 3, "carrot": 2})
take_order("Praveen", {"potato": 10, "cabbage": 2, "onion": 5})
take_order("Vinodkumar", {"tomato": 10, "potato": 15, "cabbage": 5})

# Final report
show_sales_report()
show_remaining_stock()