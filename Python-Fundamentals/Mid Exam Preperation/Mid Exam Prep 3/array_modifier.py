numbers = list(map(int, input().split()))
command = input()

while command != "end":
    params = command.split()
    action = params[0]

    if action == "swap":
        first_index = int(params[1])
        second_index = int(params[2])
        numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]

    elif action == "multiply":
        first_index = int(params[1])
        second_index = int(params[2])
        numbers[first_index] *= numbers[second_index]

    elif action == "decrease":
        numbers = [el - 1 for el in numbers]

    command = input()

print(', '.join(str(el) for el in numbers))
