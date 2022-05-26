def coffee():
    command = input()
    coffee_count = 0
    while command != "END":
        new_command = command
        if new_command.isupper():
            if new_command == "CODING":
                coffee_count += 2
            elif new_command == "DOG" or new_command == "CAT":
                coffee_count += 2
            elif new_command == "MOVIE":
                coffee_count += 2
        elif new_command.islower():
            if new_command == "coding":
                coffee_count += 1
            elif new_command == "dog" or new_command == "cat":
                coffee_count += 1
            elif new_command == "movie":
                coffee_count += 1
        else:
            continue
        command = input()

    if coffee_count > 5:
        print("You need extra sleep")
    else:
        print(coffee_count)


coffee()