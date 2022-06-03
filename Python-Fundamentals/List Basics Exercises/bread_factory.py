events = input().split("|")
max_energy = 100
energy = 100
coins = 100
closed = False

for event in events:
    event_info = event.split("-")
    action = event_info[0]
    value = int(event_info[1])
    closed = False

    if action == "rest":
        gained = min(value, max_energy - energy)
        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')

    elif action == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            closed = True
            break

if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

