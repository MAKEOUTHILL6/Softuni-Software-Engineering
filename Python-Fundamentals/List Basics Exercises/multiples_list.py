factor = int(input())
count = int(input())

new_list = []

for num in range(factor, count * factor + 1, factor):
    new_list.append(num)
print(new_list)