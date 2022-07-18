phone_dict = {}

while True:

    command = input()

    if '-' not in command:
        break

    name, phone = command.split("-")

    phone_dict[name] = phone

for __ in range(int(command)):
    person = input()
    if person in phone_dict.keys():
        print(f"{person} -> {phone_dict[person]}")
    else:
        print(f"Contact {person} does not exist")