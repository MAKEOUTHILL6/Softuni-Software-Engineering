budget_of_the_movie = float(input())
number_of_statists = int(input())
price_per_clothing = float(input())

price_for_decor = budget_of_the_movie * 0.10
price_per_clothing_for_extra = price_per_clothing * number_of_statists

if number_of_statists > 150:
    price_per_clothing_for_extra -= price_per_clothing_for_extra * 0.10

total_price = price_for_decor + price_per_clothing_for_extra

money_needed = abs(budget_of_the_movie - total_price)

if budget_of_the_movie >= total_price:
    print('Action!')
    print(f'Wingard starts filming with {money_needed:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')

