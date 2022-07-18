command = input()

company = {}

while command != "End":
    params = command.split(" -> ")
    name = params[0]
    person_id = params[1]
    if name not in company:
        company[name] = [person_id]
    else:
        if person_id not in company[name]:
            company[name].append(person_id)

    command = input()

for c in company:
    print(c)
    for ce in company[c]:
        print(f"-- {ce}")


