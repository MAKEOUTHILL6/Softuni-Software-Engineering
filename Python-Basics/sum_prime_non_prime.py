sum_prime = 0
sum_non_prime = 0
command = input()

while command != "stop":
    current = int(command)
    if current < 0:
        print("Number is negative.")
        command = input()
        continue
    else:
        number_is_prime = True
        for number in range(2, current):
            if current % number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            sum_prime += current
        else:
            sum_non_prime += current
    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")