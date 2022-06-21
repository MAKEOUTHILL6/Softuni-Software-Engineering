from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

student_attendence = []
students_points = []
temp_points = 0
for _ in range(students):
    student = int(input())
    student_attendence.append(student)
    temp_points = (student / lectures) * (5 + bonus)
    students_points.append(temp_points)

max_points = max(students_points)

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {max(student_attendence)} lectures.")