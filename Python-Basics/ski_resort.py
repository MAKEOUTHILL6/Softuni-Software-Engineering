days = int(input())
room_type = input()
review = input()

nights = days - 1
price = 0

if room_type == "room for one person":
    price = 18 * nights
elif room_type == "apartment":
    price = 25 * nights
    if days <= 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days >= 15:
        price *= 0.5 * nights
elif room_type == "president apartment":
    price = 35 * nights
    if days <= 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days >= 15:
        price *= 0.80
if review == "positive":
    total_price = price + (price * 0.25)
else:
    total_price = price - (price * 0.1)
print(f"{total_price:.2f}")
