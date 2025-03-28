def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    return price


try:
    price = 8500
    discount_percent = 25
    
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values.")
