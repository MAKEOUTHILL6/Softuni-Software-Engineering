def chars(a, b):
    chars_list = []
    for i in range(ord(a) + 1, ord(b)):
        chars_list.append(chr(i))

    return " ".join(chars_list)


char1 = input()
char2 = input()
print(chars(char1, char2))