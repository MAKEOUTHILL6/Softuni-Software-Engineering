price_excursion = float(input())
puzzels = int(input())
dolls = int(input())
teddybear = int(input())
minions = int(input())
truck = int(input())

total_sum = puzzels * 2.60 + dolls * 3 + teddybear * 4.10 + minions * 8.20 + truck * 2
toys_quantity = puzzels + dolls + teddybear + minions + truck

if toys_quantity >= 50:
    total_sum = total_sum - (total_sum * 0.25)

rent = total_sum * 0.10

Winnings = total_sum - rent

diff = abs(Winnings - price_excursion)

if Winnings >= price_excursion:
    print(f'Yes! {diff:.2f} lv. left.')
else:
    print(f'Not enough money! {diff:.2f} lv. needed.')