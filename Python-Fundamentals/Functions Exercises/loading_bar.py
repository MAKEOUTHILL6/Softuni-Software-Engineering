def loading_bar_creation(number):
    charging_bar = []
    charge = number // 10

    for i in range(charge):
        charging_bar.append("%")

    while len(charging_bar) != 10:
        for c in range(charge + 1, 10 + 1):
            charging_bar.append(".")
    return "".join(charging_bar)


def loading(number):
    if number < 100:
        print(f"{number}% [{loading_bar_creation(number)}]")
        print("Still loading...")
    elif number == 100:
        print(f"{number}% Complete!")
        print(f"[{loading_bar_creation(number)}]")


num = int(input())
loading(num)
