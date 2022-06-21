command = input()
total_price_parts = 0
while command != "special" and command != "regular":
    prices = float(command)
    if prices < 0:
        print("Invalid price!")
        command = input()
        continue

    total_price_parts += prices

    command = input()

taxes = total_price_parts * 0.2
total_price = taxes + total_price_parts

if total_price <= 0:
    print("Invalid order!")
    exit()
else:
    if command == "special":
        total_price *= 0.9

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price_parts:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print("-----------")
print(f"Total price: {total_price:.2f}$")
