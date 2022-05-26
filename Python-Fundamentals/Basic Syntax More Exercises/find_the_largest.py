number = int(input())
number_as_str = str(number)
new_num = "".join(sorted(number_as_str, reverse=True))
print(new_num)