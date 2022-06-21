pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_section_health = int(input())
command = input()
retired = True
while command != "Retire":
    params = command.split()
    action = params[0]

    if action == "Fire":
        fired_index = int(params[1])
        damage = int(params[2])
        if fired_index >= 0 and fired_index < len(war_ship):
            war_ship[fired_index] -= damage
            if war_ship[fired_index] <= 0:
                retired = False
                print("You won! The enemy ship has sunken.")
                break

    elif action == "Defend":
        start_index = int(params[1])
        end_index = int(params[2])
        damage = int(params[3])
        if start_index >= 0 and start_index < len(pirate_ship) and end_index >= 0 and end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    retired = False
                    print("You lost! The pirate ship has sunken.")
                    break

    elif action == "Repair":
        repair_index = int(params[1])
        repaired_health = int(params[2])
        if repair_index < len(pirate_ship) and repair_index >= 0:
            if repaired_health + pirate_ship[repair_index] > max_section_health:
                pirate_ship[repair_index] = max_section_health
            else:
                pirate_ship[repair_index] += repaired_health

    elif action == "Status":
        count = 0
        for section in range(len(pirate_ship)):
            percentage_section = abs(pirate_ship[section] / max_section_health) * 100
            if percentage_section < 20:  # for x in pirate_ship: if x < max_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    command = input()

if retired:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
