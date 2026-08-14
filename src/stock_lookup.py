#!/usr/bin/env python3
"""
Stock lookup script - Issue #7
Given a SKU, returns whether it's in stock and the quantity.
"""
import json
import sys

DATA_FILE = "data/stock.json"

def load_stock():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def lookup(sku, stock):
    item = stock.get(sku)
    if item is None:
        return {"sku": sku, "found": False, "message": "SKU not found"}
    return {
        "sku": sku,
        "found": True,
        "name": item["name"],
        "in_stock": item["in_stock"],
        "quantity": item["quantity"],
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 src/stock_lookup.py <SKU>")
        sys.exit(1)

    sku = sys.argv[1]
    stock = load_stock()
    result = lookup(sku, stock)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
