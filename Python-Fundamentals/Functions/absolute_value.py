numbers = input().split()
numbers_as_digit = list(map(float, numbers))
abs_list = []
for nums in numbers_as_digit:
    abs_list.append(abs(nums))
print(abs_list)