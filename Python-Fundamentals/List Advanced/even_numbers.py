numbers = input().split(", ")
numbers_as_digit = list(map(int, numbers))
even_list = []

for num in numbers_as_digit:
    if num % 2 == 0:
        index = numbers_as_digit.index(num)
        even_list.append(index)

print(even_list)