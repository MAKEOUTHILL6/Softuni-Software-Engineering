numbers = input().split()
numbers_as_digit = list(map(int, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers_as_digit))
print(filtered)