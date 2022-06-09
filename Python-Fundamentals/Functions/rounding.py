def func(number):
    rounded_list = list(map(round, number))

    print(rounded_list)


numbers = input().split()
numbers_as_digit = list(map(float, numbers))
func(numbers_as_digit)