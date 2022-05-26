excursion_price = float(input())
money_available = float(input())

days_gone = 0
spending_counter = 0
is_spending = False
while money_available < excursion_price:
    action = input()
    money = float(input())
    days_gone += 1
    if action == "spend":
        money_available -= money
        spending_counter += 1

        if money_available <= 0:
            money_available = 0

        elif spending_counter == 5:
            is_spending = True
            break

    elif action == "save":
        money_available += money
        spending_counter = 0

if is_spending:
    print("You can't save the money.")
    print(days_gone)
else:
    print(f"You saved the money for {days_gone} days.")
