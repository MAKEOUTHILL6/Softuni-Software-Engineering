def multiple(divisor, boundary):
    largest = 0
    for number in range(1, boundary + 1):
        if number % divisor == 0:
            if number > 0:
                if number <= boundary:
                    if number > largest:
                        largest = 0
                        largest += number
    print(largest)

divisor = int(input())
boundary = int(input())
multiple(divisor, boundary)