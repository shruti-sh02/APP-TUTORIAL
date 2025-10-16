def discount_calculator(rate):
    def apply_discount(price):
        return price * (1 - rate)
    return apply_discount

# Example
ten_percent = discount_calculator(0.1)
print(ten_percent(2000))  # Output: 1800.0
