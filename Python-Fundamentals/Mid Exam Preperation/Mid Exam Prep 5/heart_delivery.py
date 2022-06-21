sequence = list(map(int, input().split("@")))
command = input()
is_successful = False
cupid_position = 0
while command != "Love!":
    params = command.split()
    action = params[0]
    jump_length = int(params[1])

    if action == "Jump":
        for house in range(len(sequence)):
            cupid_position += house + jump_length
            if cupid_position >= len(sequence):
                cupid_position = 0
            if sequence[cupid_position] == 0:
                print(f"Place {cupid_position} already had Valentine's day.")
                break

            sequence[cupid_position] -= 2
            if sequence[cupid_position] == 0:
                print(f"Place {cupid_position} has Valentine's day.")

            break

    command = input()

print(f"Cupid's last position was {cupid_position}.")
count = sequence.count(0)
if count == len(sequence):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(sequence) - count} places.")
