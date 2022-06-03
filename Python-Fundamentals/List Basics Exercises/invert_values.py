normal_list = input().split()
reversed_list = []

for num in normal_list:
    opposite = -int(num)
    reversed_list.append(opposite)

print(reversed_list)