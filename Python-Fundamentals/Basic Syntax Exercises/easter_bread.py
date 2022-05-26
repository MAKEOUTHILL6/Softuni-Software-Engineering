budget = float(input())
kg_flour_price = float(input())
pack_eggs_price = kg_flour_price * 0.75    # kg_price_flour - (0.75 * kg_price_flour)
liter_milk_price = kg_flour_price + (kg_flour_price * 0.25)
quater_milk_price = liter_milk_price / 1/4
count = 1
colored_eggs = 0

while budget > 0:
    for i in range(count):
        loaf_price = quater_milk_price + pack_eggs_price + kg_flour_price
        count += 1
        colored_eggs += 3
        budget -= loaf_price
        if i % 3 == 0:
            colored_eggs = count - 2
print(f"You made {count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")