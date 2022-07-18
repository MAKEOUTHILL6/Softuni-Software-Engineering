def finished(words_dict):
    res = ''
    for w in words_dict:
        if words_dict[w] % 2 != 0:
            res += w + " "
    return res


words = input().split()
words_dict = {}
for word in words:
    word = word.lower()
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1


print(finished(words_dict))