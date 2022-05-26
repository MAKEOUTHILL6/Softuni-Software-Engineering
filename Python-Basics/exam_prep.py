fail_threshold = int(input())


average_score = 0
all_exercises = 0
has_failed = True
failed_count = 0
last_problem = ""

while failed_count < fail_threshold:
    name_of_exercises = input()
    if name_of_exercises == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_count += 1
    average_score += grade
    last_problem = name_of_exercises
    all_exercises += 1


if has_failed == False:
    print(f"Average score: {average_score / all_exercises:.2f}")
    print(f"Number of problems: {all_exercises}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {fail_threshold} poor grades.")
