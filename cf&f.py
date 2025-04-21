def calculate_discount(price, discount_percent):

    price = int(input("Enter the price: "))
    discount_percent = int(input("Enter the discount_percent: "))

    calculated_discount = price - (price * discount_percent / 100)

    if discount_percent < 0:
        return f"The discount_percent cannot be negative"
    elif discount_percent > 100:
        return f"The discount_percent cannot be greater than 100"

    elif discount_percent < 20 and discount_percent > 0:
        return f"The discount_percent is less than 20%"
    elif discount_percent == 0:
        return f"You did not apply any discount\nThe price is: {price}"
    elif discount_percent >= 20:
        return f"The price after discount is: {calculated_discount}"


sale = calculate_discount('price', 'discount_percent')
print(sale)
print("Enjoy your purchase!")
