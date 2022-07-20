def char_position(letter):
    return ord(letter.lower()) - 97 + 1


def getting_result(elements):
    numbers = [num for num in elements if num.isdigit()]
    res = 0
    numbers = int(''.join(numbers))
    for el in range(len(elements)):
        if elements[el].isalpha():
            alphabet_pos = char_position(elements[el])

            if el == 0:
                if elements[el].isupper():
                    res = numbers / alphabet_pos

                else:
                    res = numbers * alphabet_pos

            else:
                if elements[el].isupper():
                    res -= alphabet_pos

                else:
                    res += alphabet_pos

    return res


text = input().split()
results = []

res = 0
for elements in text:
    res += getting_result(elements)

print(f'{res:.2f}')






