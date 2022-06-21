workers_list = []
for _ in range(3):
    workers_list.append(int(input()))

students = int(input())
hours = 0
while students:
    for worker in workers_list:
        if students == 0:
            continue
        students -= worker
    hours += 1
    if hours % 4 == 0 and hours != 0:
        hours += 1


print(f"Time needed: {hours}h.")