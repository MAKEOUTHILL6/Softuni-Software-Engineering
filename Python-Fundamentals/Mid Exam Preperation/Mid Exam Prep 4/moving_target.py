targets = list(map(int, input().split()))
command = input()


def strike_func(targets, index, radius):
    targets[index + radius] = 0
    targets[index - radius] = 0
    targets[index] = 0
    result = [el for el in targets if el != 0]

    return result


while command != "End":
    params = command.split()
    action = params[0]
    index = int(params[1])

    if action == "Shoot":
        power = int(params[2])
        if index < len(targets) and index >= 0:
            if targets[index] > 0:
                targets[index] -= power
                if targets[index] <= 0:
                    targets.pop(index)

    elif action == "Add":
        value = int(params[2])
        if index < len(targets) and index >= 0:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(params[2])
        if 0 <= index - radius < len(targets) and 0 <= index + radius < len(targets):
            targets = strike_func(targets, index, radius)
        else:
            print("Strike missed!")
            command = input()
            continue

    command = input()


print("|".join(str(el) for el in targets))