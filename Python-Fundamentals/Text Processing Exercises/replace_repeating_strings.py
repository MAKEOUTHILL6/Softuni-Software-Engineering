text = input()
res = []
count = 0
for word in range(len(text)):
    el = text[word]
    last_word = text[word - 1]
    if text[word] != last_word:
        res.append(text[word])
print(res)
