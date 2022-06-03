numbers = input().split()
copy_numbers = list(map(int, numbers))
remover = int(input())

for r in range(remover):
    min_number = min(copy_numbers)
    numbers.remove(str(min_number))
    copy_numbers.remove(min_number)
print(", ".join(numbers))