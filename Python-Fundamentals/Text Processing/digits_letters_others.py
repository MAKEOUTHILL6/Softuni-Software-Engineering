word = input()
numbers = []
letters = []
symbols = []

for el in word:
    if el.isdigit():
        numbers.append(el)

    elif el.isalpha():
        letters.append(el)

    else:
        symbols.append(el)

print(''.join(numbers))
print(''.join(letters))
print(''.join(symbols))