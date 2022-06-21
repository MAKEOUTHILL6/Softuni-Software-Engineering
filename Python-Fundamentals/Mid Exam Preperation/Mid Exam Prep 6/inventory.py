items = input().split(", ")
command = input()

while command != "Craft!":
    params = command.split(" - ")
    action = params[0]

    if action == "Collect":
        collected_item = params[1]
        if collected_item not in items:
            items.append(collected_item)

    elif action == "Drop":
        dropped_item = params[1]
        if dropped_item in items:
            items.remove(dropped_item)

    elif action == "Combine Items":
        new_params = params[1].split(":")
        old_item = new_params[0]
        new_item = new_params[1]
        if old_item in items:
            index_old_item = items.index(old_item)
            items.insert(index_old_item + 1, new_item)

    elif action == "Renew":
        renewed_item = params[1]
        if renewed_item in items:
            items.append(renewed_item)
            items.remove(renewed_item)

    command = input()

print(', '.join(items))