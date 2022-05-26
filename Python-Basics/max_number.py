import sys
input_line = input()

max_number = -sys.maxsize
while input_line != "Stop":
    current_num = int(input_line)

    if current_num > max_number:
        max_number = current_num

    input_line = input()
print(max_number)
