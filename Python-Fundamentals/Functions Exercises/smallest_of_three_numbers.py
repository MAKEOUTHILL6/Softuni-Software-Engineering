num1 = int(input())
num2 = int(input())
num3 = int(input())

num_list = []

while len(num_list) != 3:
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
print(min(num_list))
