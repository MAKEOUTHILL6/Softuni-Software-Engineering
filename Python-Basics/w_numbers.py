number1 = int(input())
number2 = int(input())
operator = input()

result = 0
odd_or_even = "odd"

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    if result % 2 == 0:
        odd_or_even = "even"
    print(f"{number1} {operator} {number2} = {result} - {odd_or_even}")

else:
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")

    elif operator == "/":
        result = number1 / number2
        print(f"{number1} {operator} {number2} = {result:.2f}")

    elif operator == "%":
        result = number1 % number2
        print(f"{number1} {operator} {number2} = {result}")
