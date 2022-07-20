text = input()
res = ''
for word in text:
    word = ord(word) + 3
    res += chr(word)
print(res)