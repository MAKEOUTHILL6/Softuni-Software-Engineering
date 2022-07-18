def get_info(phonebook_dict, command):
    for x in range(command):
        name = input()
        if name in phonebook_dict.keys():
            print(f"{name} -> {phonebook_dict[name]}")
        else:
            print(f"Contact {name} does not exist.")

    return True


phonebook_dict = {}
condition = False

while True:
    command = input().split("-")

    if command[0].isdigit():
        command = "".join(command)
        command = int(command)
        condition = get_info(phonebook_dict, command)
    else:
        phonebook_dict[command[0]] = command[1]

    if condition:
        break




