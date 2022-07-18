minerals_dict = {}

command = input()
while command != "stop":
    if command not in minerals_dict.keys():
        minerals_dict[command] = 0
    resource_mat = int(input())
    minerals_dict[command] += int(resource_mat)
    command = input()

for key, value in minerals_dict.items():
    print(f"{key} -> {value} ")