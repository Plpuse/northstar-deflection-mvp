"""
Stock lookup CLI - Issue #8
Interactive command-line wrapper around stock_lookup.py.
Lets a user type a SKU and get a plain-English stock status.
"""
from stock_lookup import load_stock, lookup


def format_response(result):
    if not result["found"]:
        return f"Sorry, we couldn't find SKU '{result['sku']}'."
    if result["in_stock"]:
        return f"{result['name']} ({result['sku']}) is IN STOCK - {result['quantity']} available."
    return f"{result['name']} ({result['sku']}) is OUT OF STOCK."


def main():
    stock = load_stock()
    print("Stock Lookup CLI - type a SKU to check status, or 'quit' to exit.")
    while True:
        sku = input("SKU> ").strip()
        if sku.lower() == "quit":
            break
        if not sku:
            continue
        result = lookup(sku, stock)
        print(format_response(result))


if __name__ == "__main__":
    main()
