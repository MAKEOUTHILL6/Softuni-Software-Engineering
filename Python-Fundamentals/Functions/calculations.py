def func(action, fnum, snum):
    result = 0
    if action == "multiply":
        result += fnum * snum
    elif action == "divide":
        result += fnum // snum
    elif action == "subtract":
        result += fnum - snum
    else:
        result += fnum + snum
    return result
action = input()
num1 = int(input())
num2 = int(input())

print(func(action, num1, num2))