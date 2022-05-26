budget = int(input())
season = input()
fishermen = int(input())

price_per_season = 0
discount = 0
total_price = 0

if season == "Spring":
    price_per_season = 3000

elif season == "Autumn":
    price_per_season = 4200

elif season == "Summer":
    price_per_season = 4200

elif season == "Winter":
    price_per_season = 2600

if fishermen <= 6:
    price_per_season *= 0.9

elif fishermen <= 11:
    price_per_season *= 0.85

elif fishermen > 12:
    price_per_season *= 0.75

if season != "Autumn" and fishermen %2 == 0:
    price_per_season *= 0.95

diff = abs(budget - price_per_season)

if budget >= price_per_season:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")