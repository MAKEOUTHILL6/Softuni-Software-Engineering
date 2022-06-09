numbers = input().split(", ")
numbers_as_digit = list(map(int, numbers))
for element in range(len(numbers_as_digit)):
    if numbers_as_digit[element] == 0:
        numbers_as_digit.remove(numbers_as_digit[element])
        numbers_as_digit.append(0)
print(numbers_as_digit)