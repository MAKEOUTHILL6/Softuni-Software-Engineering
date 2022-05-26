free_width = int(input())
free_length = int(input())
free_height = int(input())

free_space_available = free_height * free_length * free_width
is_filled = True
command = input()
while command != "Done":
    current_space = int(command)
    free_space_available -= current_space

    if free_space_available <= 0:
        is_filled = False
        break
    command = input()


if is_filled:
    print(f"{abs(free_space_available)} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space_available)} Cubic meters more.")