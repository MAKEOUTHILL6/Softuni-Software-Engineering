fire_cells = input().split("#")
water_quantity = int(input())
effort = 0
total_fire = 0
water_wasted = 0
print("Cells: ")
for current_fire in fire_cells:
    fire_info = current_fire.split(" = ")
    fire_type = fire_info[0]
    fire_value = int(fire_info[1])
    extinguished = False

    if fire_type == "High":
        if water_quantity >= fire_value:
            if 81 <= fire_value <= 125:
                water_quantity -= fire_value
                effort += fire_value * 0.25
                total_fire += fire_value
                extinguished = True

    elif fire_type == "Medium":
        if water_quantity >= fire_value:
            if 51 <= fire_value <= 80:
                water_quantity -= fire_value
                effort += fire_value * 0.25
                total_fire += fire_value
                extinguished = True

    elif fire_type == "Low":
        if water_quantity >= fire_value:
            if 1 <= fire_value <= 50:
                water_quantity -= fire_value
                effort += fire_value * 0.25
                total_fire += fire_value
                extinguished = True

    if extinguished:
        print(f"- {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")