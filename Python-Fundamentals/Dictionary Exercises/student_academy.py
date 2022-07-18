lines = int(input())

students = {}


for _ in range(lines):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = grade
    else:
        students[name] += grade
        students[name] /= 2


for name in students:
    if students[name] >= 4.50:
        print(f"{name} -> {students[name]:.2f}")