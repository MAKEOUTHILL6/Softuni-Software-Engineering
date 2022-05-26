lines = int(input())
water_tank_capacity = 255
poured_litters = 0
for i in range(lines):
    water = int(input())
    if water + poured_litters > 255:
        print("Insufficient capacity!")
        continue
    poured_litters += water
print(poured_litters)