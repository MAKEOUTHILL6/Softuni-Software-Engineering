products = input().split()
searched_products = input().split()
shop = {}
for el in range(0, len(products), 2):
    key = products[el]
    value = products[el+1]
    shop[key] = value

for pro in searched_products:
    if pro in shop.keys():
        print(f"We have {shop[pro]} of {pro} left")
    else:
        print(f"Sorry, we don't have {pro}")