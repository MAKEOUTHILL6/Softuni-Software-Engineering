command = input()
courses = {}
while command != "end":
    params = command.split(" : ")
    course = params[0]
    name = params[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(name)

    command = input()

for c in courses:
    print(f"{c}: {len(courses[c])}")
    res = ''
    for ce in courses[c]:
        res += f"-- {ce}"
        print(res)
        res = ''
