def todo():
    events = ["0"] * 10
    command = input()
    while command != "End":
        command_info = command.split('-')
        importance = int(command_info[0])
        action = command_info[1]
        events.pop(importance)
        events.insert(importance, action)

        command = input()

    result = [el for el in events if el != "0"]
    print(result)


todo()