items = input().split("|")
budget = float(input())
sum_old = 0
sum_new = 0
new_price = []
new_price_rounded = []
train_ticket = 150
profit = 0

for item in items:
    item_info = item.split("->")
    item_type = item_info[0]
    item_price = float(item_info[1])
    bought = False

    if item_type == "Clothes":
        if budget >= item_price:
            if item_price <= 50:
                budget -= item_price
                sum_old += item_price
                bought = True

                if bought:
                    new = item_price + (item_price * 0.4)
                    sum_new += new
                    new_price.append(new)

    elif item_type == "Shoes":
        if budget >= item_price:
            if item_price <= 35:
                budget -= item_price
                sum_old += item_price
                bought = True

                if bought:
                    new = item_price + (item_price * 0.4)
                    sum_new += new
                    new_price.append(new)

    elif item_type == "Accessories":
        if budget >= item_price:
            if item_price <= 20.50:
                budget -= item_price
                sum_old += item_price
                bought = True

                if bought:
                    new = item_price + (item_price * 0.4)
                    sum_new += new
                    new_price.append(new)

for money in new_price:
    n = f"{money:.2f}"
    new_price_rounded.append(n)

profit = abs(sum_new - sum_old)

print(" ".join(new_price_rounded))
print(f"Profit: {profit:.2f}")

if sum_new + budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")