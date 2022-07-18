force_side_dict = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        params = command.split(" | ")
        force_side, force_user = params
        present = False
        for value in force_side_dict.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)

    else:
        params = command.split(" -> ")
        force_user, force_side = params
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break

        if force_side not in force_side_dict:
            force_side_dict[force_side] = [force_user]
        else:
            force_side_dict[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key in force_side_dict:
    if len(force_side_dict[key]) > 0:
        print(f"Side: {key}, Members: {len(force_side_dict[key])}")
        [print(f"! {user}") for user in force_side_dict[key]]