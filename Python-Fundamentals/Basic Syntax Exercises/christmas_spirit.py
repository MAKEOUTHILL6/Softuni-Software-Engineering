quantity = int(input())
remaining_days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0

for day in range(1, remaining_days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        ornament_set = ornament_set_price * quantity
        total_cost += ornament_set
        total_spirit += 5
    if day % 3 == 0:
        tree_skirt = tree_skirt_price * quantity
        tree_garlands = tree_garlands_price * quantity
        total_cost += tree_garlands + tree_skirt    # total_cost += (tree_garlands + tree_skirt) * quantity
        total_spirit += 13
    if day % 5 == 0:
        tree_lights = tree_lights_price * quantity
        total_cost += tree_lights
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_lights_price + tree_skirt_price + tree_garlands_price
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")