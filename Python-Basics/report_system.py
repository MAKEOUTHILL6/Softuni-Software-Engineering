sales_amount = int(input())

command = input()
count_cash = 0
count_card = 0
total_cash = 0
total_card = 0
counter = 0
sum_collected = False
total_amount = 0
while command != "End":
    product_price = int(command)
    counter += 1
    if counter % 2 == 1:
        if product_price > 100:
            print("Error in transaction!")
        else:
            count_cash += 1
            total_cash += product_price
            print("Product sold!")
            total_amount += product_price

    else:
        if product_price < 10:
            print("Error in transaction!")
        else:
            count_card += 1
            total_card += product_price
            print("Product sold!")
            total_amount += product_price

    if total_amount >= sales_amount:
        sum_collected = True
        break
    command = input()

if sum_collected:
    print(f"Average CS: {total_cash / count_cash:.2f}")
    print(f"Average CC: {total_card / count_card:.2f}")
else:
    print("Failed to collect required money for charity.")




