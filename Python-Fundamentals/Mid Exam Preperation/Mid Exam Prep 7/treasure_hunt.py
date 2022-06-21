treasure = input().split("|")
command = input()

while command != "Yohoho!":
    params = command.split()
    action = params[0]

    if action == "Loot":
        for i in range(1, len(params)):
            collected_items = params[i]
            if collected_items not in treasure:
                treasure.insert(0, collected_items)

    elif action == "Drop":
        index = int(params[1])
        if index >= 0 and index < len(treasure):
            treasure.append(treasure.pop(index))

    elif action == "Steal":
        count = int(params[1])
        stolen_items = []
        if count < len(treasure):
            for i in range(-count, -0):
                item_index = treasure.pop(i)
                stolen_items.append(item_index)

        else:
            stolen_items = [item for item in treasure]
            treasure = []
        print(', '.join(stolen_items))

    command = input()

length_names_sum = 0
for item in treasure:
    length_names_sum += len(item)

if treasure:
    average_treasure_gain = length_names_sum / len(treasure)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")