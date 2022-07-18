command = input()
products = {}
while command != "buy":
    params = command.split()
    product = params[0]
    price = float(params[1])
    quantity = int(params[2])
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product] = [price, quantity + products[product][1]]

    command = input()

for order in products:
    total_sum = products[order][0] * products[order][1]
    print(f"{order} -> {total_sum:.2f}")
