from collections import deque

groceries = deque(input().split("!"))
command = input()

while command != "Go Shopping!":
    params = command.split()
    action = params[0]
    item = params[1]

    if action == "Urgent":
        if item not in groceries:
            groceries.appendleft(item)

    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    elif action == "Correct":
        new_item = params[2]
        if item in groceries:
            ind = groceries.index(item)
            groceries[ind] = new_item

    elif action == "Rearrange":
        if item in groceries:
            groceries.append(item)
            groceries.remove(item)

    command = input()

print(", ".join(str(x) for x in groceries))