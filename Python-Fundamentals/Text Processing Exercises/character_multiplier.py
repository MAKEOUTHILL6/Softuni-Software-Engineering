def sum_func(first, second):
    total_sum = 0
    for i in range(len(first)):
        if i < len(second):
            total_sum += ord(first[i]) * ord(second[i])
        else:
            total_sum += ord(first[i])

    return total_sum


def char_multiplier(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = sum_func(first_word, second_word)

    else:
        result = sum_func(second_word, first_word)

    print(result)


data = input().split()
char_multiplier(data[0], data[1])
