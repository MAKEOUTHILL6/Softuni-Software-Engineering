def perfect_num(number):
    sum = 0

    for numb in range(1, number + 1):
        if number % numb == 0:
            if sum != number:
                sum += numb
    if sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(perfect_num(num))