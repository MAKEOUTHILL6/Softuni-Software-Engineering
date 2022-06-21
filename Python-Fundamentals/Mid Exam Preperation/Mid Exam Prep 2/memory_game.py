sequence = input().split()
command = input()
moves_made = 0
is_successful = False
while command != "end":
    info_params = command.split()
    first_index = int(info_params[0])
    second_index = int(info_params[1])
    moves_made += 1

    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(sequence) or \
            second_index >= len(sequence):
        middle_of_seq = len(sequence) // 2
        sequence.insert(middle_of_seq, f"-{moves_made}a")
        sequence.insert(middle_of_seq + 1, f"-{moves_made}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence[first_index] == sequence[second_index]:
        el = sequence.pop(first_index)
        sequence.remove(el)
        print(f"Congrats! You have found matching elements - {el}!")
    else:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {moves_made} turns!")
        break

    command = input()

if command == "end":
    print("Sorry you lose :(")
    print(" ".join(str(el) for el in sequence))

