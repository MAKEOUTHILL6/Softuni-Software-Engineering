targets = list(map(int, input().split()))
command = input()
shot_targets = 0
while command != "End":
    index = int(command)
    current_target = 0
    if 0 <= index < len(targets):
        if targets[index] >= 0:
            current_target = targets[index]
            targets[index] = -1
            shot_targets += 1

        for target in range(len(targets)):
            if targets[target] >= 0:
                if targets[target] > current_target:
                    targets[target] -= current_target
                elif targets[target] <= current_target:
                    targets[target] += current_target

    command = input()

print(f"Shot targets: {shot_targets} -> {' '.join(str(el) for el in targets)}")