def hogwarts():
    command = input()
    student_list = []
    count = 0
    successful = True
    while command != "Welcome!":
        name = command
        if name == "Voldemort":
            print("You must not speak of that name!")
            successful = False
            break

        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
            student_list.append(name)
            count += 1
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
            student_list.append(name)
            count += 1
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
            student_list.append(name)
            count += 1
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")
            student_list.append(name)
            count += 1
        command = input()

    if successful:
        if count == len(student_list):
            print("Welcome to Hogwarts.")


hogwarts()