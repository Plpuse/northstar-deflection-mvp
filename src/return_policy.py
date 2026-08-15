#!/usr/bin/env python3

"""
Return policy decision tree.

Given an order's return details, determines whether the item
is eligible for a return and explains why.
"""


def check_return_policy(
    days_since_delivery,
    item_condition,
    return_reason,
    is_final_sale=False,
):
    """
    Apply the return policy decision tree.

    Scenarios covered:
    1. Item is within the return window and acceptable condition.
    2. Item is outside the return window.
    3. Item is final sale.
    4. Item is damaged/defective.
    5. Item has been used.
    """

    # Final-sale items cannot be returned.
    if is_final_sale:
        return {
            "eligible": False,
            "decision": "REJECT",
            "reason": "Final-sale items are not eligible for return.",
        }

    # Damaged or defective items are accepted even if outside
    # the normal return window.
    if return_reason.lower() in ["damaged", "defective"]:
        return {
            "eligible": True,
            "decision": "ACCEPT",
            "reason": "Damaged or defective item qualifies for a return.",
        }

    # Normal returns must be requested within 30 days.
    if days_since_delivery > 30:
        return {
            "eligible": False,
            "decision": "REJECT",
            "reason": "Return request is outside the 30-day return window.",
        }

    # Item must be in acceptable condition.
    if item_condition.lower() not in ["new", "unused", "like_new"]:
        return {
            "eligible": False,
            "decision": "REJECT",
            "reason": "Item must be new, unused, or like new.",
        }

    return {
        "eligible": True,
        "decision": "ACCEPT",
        "reason": "Item meets the standard return policy.",
    }


def main():
    test_cases = [
        {
            "name": "Normal return",
            "days_since_delivery": 10,
            "item_condition": "new",
            "return_reason": "changed_mind",
            "is_final_sale": False,
        },
        {
            "name": "Late return",
            "days_since_delivery": 45,
            "item_condition": "new",
            "return_reason": "changed_mind",
            "is_final_sale": False,
        },
        {
            "name": "Damaged item",
            "days_since_delivery": 45,
            "item_condition": "damaged",
            "return_reason": "damaged",
            "is_final_sale": False,
        },
        {
            "name": "Final sale",
            "days_since_delivery": 5,
            "item_condition": "new",
            "return_reason": "changed_mind",
            "is_final_sale": True,
        },
    ]

    for case in test_cases:
        result = check_return_policy(
            case["days_since_delivery"],
            case["item_condition"],
            case["return_reason"],
            case["is_final_sale"],
        )

        print(f"\n{case['name']}")
        print(result)


if __name__ == "__main__":
    main()
