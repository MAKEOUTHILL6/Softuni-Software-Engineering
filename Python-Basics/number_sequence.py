import sys

n = int(input())

biggest_num = -sys.maxsize
lowest_num = sys.maxsize

for i in range(1, n + 1):
    value = int(input())

    if value > biggest_num:
        biggest_num = value

    if value < lowest_num:
        lowest_num = value
print(f"Max number: {biggest_num}")
print(f"Min number: {lowest_num}")

