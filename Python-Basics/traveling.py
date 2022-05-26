command = input()

while command != "End":
    price_trip = float(input())

    sum = 0
    while sum < price_trip:
        saved_money = float(input())
        sum += saved_money

    print(f"Going to {command}!")

    command = input()