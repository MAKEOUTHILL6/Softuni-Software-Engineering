jury_numbers = int(input())
name_presentation = input()

average_grade_all_presentations = 0
sum_grades = 0
grades_counter = 0

while name_presentation != "Finish":

    average_grade_per_presentation = 0

    for grades in range(jury_numbers):
        grade = float(input())
        grades_counter += 1
        sum_grades += grade
        average_grade_per_presentation = sum_grades / jury_numbers

    print(f"{name_presentation} - {average_grade_per_presentation:.2f}.")

    average_grade_all_presentations += sum_grades
    sum_grades = 0

    name_presentation = input()

print(f"Student's final assessment is {average_grade_all_presentations / grades_counter:.2f}.")