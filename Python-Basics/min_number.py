import sys
input_line = input()

min_number = sys.maxsize
while input_line != "Stop":
    current_num = int(input_line)

    if current_num < min_number:
        min_number = current_num

    input_line = input()
print(min_number)
