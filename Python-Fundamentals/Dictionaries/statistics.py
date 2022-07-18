command = input()
products = {}
while command != "statistics":
    params = command.split(": ")
    key = params[0]
    value = params[1]
    if key in products.keys():
        products[key] += int(value)
    else:
        products[key] = int(value)

    command = input()

products_l = len(products)
products_sum = sum(products.values())


def product_info(products_l, products_sum, products):
    res = "Products in stock:"
    for key, value in products.items():
        res += "\n" + f"- {key}: {value}"
    res += f"\nTotal Products: {products_l}\n"
    res += f"Total Quantity: {products_sum}"

    return res


print(product_info(products_l, products_sum, products))