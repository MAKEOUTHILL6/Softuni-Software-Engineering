names = input().split(", ")
order_list = sorted(names, key=lambda x: (-len(x), x))
print(order_list)