numbers = input().split()
numbers_as_digits = list(map(int, numbers))
string = input()
taken_num = ""
sum_list = []
word_list = []
current_sum = 0
for num in numbers:
    taken_num += num
    sum_list = [int(num) for num in str(taken_num)]
    current_sum = sum(sum_list)
    current_sum %= len(string)
    taken_num = ''
    sum_list = []
    word_list.append(string[current_sum])
    string = string.replace(string[current_sum], "", 1)
print("".join(word_list))
