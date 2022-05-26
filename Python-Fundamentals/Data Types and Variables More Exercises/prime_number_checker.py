number = int(input())

prime = False

if number > 1:
    for num in range(2, number):
        if number % num == 0:
            prime = True
            break

if prime:
    print("False")
else:
    print("True")