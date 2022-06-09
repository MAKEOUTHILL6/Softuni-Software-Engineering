def min_calc(number):

    print(f"The minimum number is {min(number)}")


def max_calc(number):

    print(f"The maximum number is {max(number)}")


def sum_calc(number):

    print(f"The sum number is: {sum(number)}")


numbers = input().split()
numbers_as_digit = list(map(int, numbers))
min_calc(numbers_as_digit)
max_calc(numbers_as_digit)
sum_calc(numbers_as_digit)
