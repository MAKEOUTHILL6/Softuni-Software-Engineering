def func(word, count):
    repeat_string = lambda a, b: a*b
    result = repeat_string(word, count)

    return result


word = input()
count = int(input())
print(func(word, count))