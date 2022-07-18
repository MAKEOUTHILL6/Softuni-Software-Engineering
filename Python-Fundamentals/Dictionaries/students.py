command = input()
courses_list = ["programming_basics", "fundamentals", "advanced"]
courses = {}
while command not in courses_list:
    params_info = command.split(":")
    name = params_info[0]
    name_id = params_info[1]
    course = params_info[2]
    courses[name_id] = {name: course}

    command = input()

given_course = command
given_course = given_course.replace("_", " ")
for student in courses:
    if given_course in (courses[student].values()):
        name_student = ''.join((courses[student].keys()))
        print(f"{name_student} - {student}")