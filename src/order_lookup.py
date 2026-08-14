import json
import os

def lookup_order(order_id):
    """Opens data/orders.json and searches for order status by order_id."""
    file_path = os.path.join("data", "orders.json")

    # 1. Open and read the file
    try:
        with open(file_path, "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        return "Error: data/orders.json file not found."
    except json.JSONDecodeError:
        return "Error: Could not parse JSON data."

    # 2. Look up the order ID
    for order in orders:
        if order.get("order_id") == str(order_id):
            return f"Order #{order_id} Status: {order['status']} | Item: {order['item']}"

    return f"Error: Order ID '{order_id}' not found."

# Quick test run
if __name__ == "__main__":
    test_id = "1001"
    print(f"Testing lookup for {test_id}:")
    print(lookup_order(test_id))
