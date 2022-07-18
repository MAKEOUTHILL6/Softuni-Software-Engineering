lines = int(input())
parking = {}
for _ in range(lines):
    command = input().split()
    action = command[0]
    name = command[1]

    if action == 'register':
        plate = command[2]
        if name not in parking:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")

    if action == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            del parking[name]
            print(f"{name} unregistered successfully")


for name, plate in parking.items():
    print(f"{name} => {plate}")