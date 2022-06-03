money = input().split(", ")
beggars = int(input())
beggars_list = []
counter_of_index = 0
temp_sum = 0
numbers_as_digit = []

for index in range(len(money)):
    numbers_as_digit.append(int(money[index]))

while counter_of_index < beggars:
    for element in range(counter_of_index, len(numbers_as_digit), beggars):
        temp_sum += numbers_as_digit[element]
    beggars_list.append(temp_sum)
    temp_sum = 0
    counter_of_index += 1
print(beggars_list)