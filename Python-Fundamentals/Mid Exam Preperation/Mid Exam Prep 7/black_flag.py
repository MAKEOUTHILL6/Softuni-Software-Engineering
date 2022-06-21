days = int(input())
plunder_per_day = int(input())
plunder_target = int(input())

plunder_collected = 0

for day in range(1, days + 1):
    plunder_collected += plunder_per_day
    if day % 3 == 0:
        plunder_collected += plunder_per_day * 0.5

    if day % 5 == 0:
        plunder_collected -= plunder_collected * 0.3

percentage = abs(plunder_collected / plunder_target) * 100

if plunder_collected >= plunder_target:
    print(f"Ahoy! {plunder_collected:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")