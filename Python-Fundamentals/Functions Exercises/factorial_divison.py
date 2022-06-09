def factorial(first_number, second_number):
    sum_first = 1
    for number in range(1, first_number + 1):
        sum_first *= number
    sum_second = 1
    for number in range(1, second_number + 1):
        sum_second *= number

    total = sum_first // sum_second

    print(f"{total:.2f}")


num1 = int(input())
num2 = int(input())
factorial(num1, num2)