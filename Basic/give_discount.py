#Give Discount:
def apply_discount(price, discount_percentage):
    discount = price * (discount_percentage / 100)
    discounted_price = price - discount
    return discounted_price

# Example usage
original_price = 100
discount_percentage = 20
final_price = apply_discount(original_price, discount_percentage)
print(final_price)  # Output: 80.0
#Code By @Rakesh Roshan Rath