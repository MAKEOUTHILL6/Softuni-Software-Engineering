number = float(input())

if number == 0:
    print("zero", end=" ")
if abs(number) < 1 and abs(number) != 0:
    print("small", end=" ")
if abs(number) > 1000000:
    print("large", end=" ")
if number > 0:
    print("positive", end=" ")
if number < 0:
    print("negative", end=" ")
