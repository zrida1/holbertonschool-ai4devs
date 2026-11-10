def calculate_discount(price, customer_type):
    """Return the final price after applying a customer discount."""
    if price < 0:
        raise ValueError("Price cannot be negative")

    discount = 0
    if customer_type == "student":
        discount = 0.10
    elif customer_type == "member":
        discount = 0.15

    final_price = price - (price * discount)
    return round(final_price, 2)


def main():
    product_price = 100
    customer = "student"
    result = calculate_discount(product_price, customer)
    print("Final price:", result)


if __name__ == "__main__":
    main()