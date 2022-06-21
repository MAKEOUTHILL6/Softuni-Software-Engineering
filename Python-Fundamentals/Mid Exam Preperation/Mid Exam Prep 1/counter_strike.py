base_energy = int(input())
won_battles = 0
is_finished = True
command = input()

while command != "End of battle":
    command = int(command)

    if base_energy >= command:
        won_battles += 1
        base_energy -= command
        if won_battles % 3 == 0:
            base_energy += won_battles
    else:
        is_finished = False
        print(f"Not enough energy! Game ends with {won_battles} won battles and {base_energy} energy")
        break

    command = input()

if is_finished:
    print(f"Won battles: {won_battles}. Energy left: {base_energy}")