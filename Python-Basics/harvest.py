from math import floor
from math import ceil

vine_area = int(input())
grape_area = float(input())
needed_liters_wine = int(input())
count_workers = int(input())
total_grapes = vine_area * grape_area
wine = 0.4 * total_grapes / 2.5
wine_left = wine - needed_liters_wine
wine_per_person = wine_left / count_workers
wine_remaining_to_get = floor(needed_liters_wine - wine)
if wine > needed_liters_wine:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(wine_left)} liters left -> {ceil(wine_per_person)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(wine_remaining_to_get)} liters wine needed.')
