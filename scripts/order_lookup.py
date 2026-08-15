import sys
import json

def lookup_order(order_id, file_path="data/orders.json"):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            
        for order in data.get("orders", []):
            if str(order.get("order_id")) == str(order_id):
                return order
                
        return {"error": "Order not found"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    query_id = sys.argv[1] if len(sys.argv) > 1 else "1001"
    result = lookup_order(query_id)
    print(json.dumps(result, indent=2))
