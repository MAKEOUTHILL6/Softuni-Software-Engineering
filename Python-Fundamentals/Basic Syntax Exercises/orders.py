def orders(number_of_orders):
    total = 0
    for order in range(1, number_of_orders + 1):
        price = float(input())
        days = int(input())
        capsule_per_day = int(input())
        if (price < 0.01 or price > 100) or \
            (days < 1 or days > 31) or \
                (capsule_per_day < 1 or capsule_per_day > 2000):
            continue
        coffee_price = price * days * capsule_per_day
        print(f"The price for the coffee is: ${coffee_price:.2f}")
        total += coffee_price
    print(f"Total: ${total:.2f}")


number = int(input())
orders(number)