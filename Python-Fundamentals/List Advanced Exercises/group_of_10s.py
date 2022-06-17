numbers = list(map(int, input().split(", ")))

tens = [el for el in numbers if el <= 10 and el < 20]
twenties = [el for el in numbers if 20 >= el > 10]
thirties = [el for el in numbers if 30 >= el > 20]
forties = [el for el in numbers if 40 >= el > 30]
fifties = [el for el in numbers if 50 >= el > 40]
if tens:
    print(f"Group of 10's: {tens}")

print(f"Group of 20's: {twenties}")
if thirties:
    print(f"Group of 30's: {thirties}")
if forties:
    print(f"Group of 40's: {forties}")
if fifties:
    print(f"Group of 50's: {fifties}")