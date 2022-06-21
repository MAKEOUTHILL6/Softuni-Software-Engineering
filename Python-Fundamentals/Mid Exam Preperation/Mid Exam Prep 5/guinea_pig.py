food_kg = float(input())
food_gr = food_kg * 1000
hay_kg = float(input())
hay_gr = hay_kg * 1000
cover_kg = float(input())
cover_gr = cover_kg * 1000
pet_kg = float(input())
pet_gr = pet_kg * 1000
is_fed = True
day = 0

while True:
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        is_fed = False
        break
    if day == 30:
        is_fed = True
        break
    food_gr -= 300
    day += 1
    if day % 2 == 0 and day != 0:
        needed_hay = food_gr * 0.05
        hay_gr -= needed_hay

    if day % 3 == 0 and day != 0:
        cover_gr -= pet_gr / 1/3

if is_fed:
    print(f"Everything is fine! Puppy is happy! Food: {food_gr / 1000:.2f}, Hay: {hay_gr/1000:.2f}, Cover: {cover_gr/1000:.2f}.")
else:
    print("Merry must go to the pet store!")