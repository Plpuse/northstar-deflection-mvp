import json
import os

def load_refunds():
    """Loads the refund database from the JSON file."""
    # Build a reliable path relative to the project root
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'refunds.json')
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find data file at {file_path}")
        return []
        
    with open(file_path, 'r') as file:
        return json.load(file)

def lookup_refund(refund_id):
    """Searches for a specific refund ID and prints its details."""
    refunds = load_refunds()
    
    for refund in refunds:
        if refund.get("refund_id") == refund_id:
            print(f"\n--- Refund Found ---")
            print(f"Refund ID:    {refund.get('refund_id')}")
            print(f"Order ID:     {refund.get('order_id')}")
            print(f"Customer:     {refund.get('customer_name')}")
            print(f"Amount:       ${refund.get('amount'):.2f}")
            print(f"Status:       {refund.get('status')}")
            print(f"Reason:       {refund.get('reason')}")
            return refund
            
    print(f"\nNotice: No refund found with ID '{refund_id}'.")
    return None

if __name__ == "__main__":
    # Test lookup with a sample refund ID
    test_id = "REF-1001"
    print(f"Searching database for refund: {test_id}...")
    lookup_refund(test_id)