def calc(num):
    even_list = []
    odd_list = []
    for n in num:
        if int(n) % 2 == 0:
            even_list.append(int(n))
        else:
            odd_list.append(int(n))

    return f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}"


number = input()
print(calc(number))
