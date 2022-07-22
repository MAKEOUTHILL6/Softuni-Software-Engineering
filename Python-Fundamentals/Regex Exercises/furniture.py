import re

pattern = r'^>>([A-Za-z]+)<<([0-9\.]+)!(\d+)'
bought_furniture = []
total_sum = 0
text = input()
while text != "Purchase":
    match = re.search(pattern, text)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_sum += float(price) * int(quantity)

    text = input()
print("Bought furniture:")
[print(x) for x in bought_furniture]
print(f"Total money spend: {total_sum:.2f}")