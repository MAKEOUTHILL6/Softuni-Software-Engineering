def trains(wagons):
    train = []
    for wagon in range(wagons):
        wagon = 0
        train.append(wagon)

    command = input()
    while command != "End":
        command_info = command.split()
        action = command_info[0]

        if action == "add":
            people_added = int(command_info[1])
            train[-1] += people_added

        elif action == "insert":
            index_insert = int(command_info[1])
            people = int(command_info[2])
            train[index_insert] += people

        elif action == "leave":
            index = int(command_info[1])
            people_left = int(command_info[2])
            train[index] -= people_left

        command = input()
    print(train)


wagons = int(input())
trains(wagons)