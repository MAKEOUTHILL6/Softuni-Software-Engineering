def func(product, count):
    price = 0
    if product == "coffee":
        price += count * 1.50
    elif product == "water":
        price += count * 1
    elif product == "coke":
        price += count * 1.40
    elif product == "snacks":
        price += count * 2

    return f'{price:.2f}'


products = input()
quantity = int(input())
print(func(products, quantity))