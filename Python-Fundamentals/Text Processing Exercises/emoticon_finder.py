text = input()
res = []
for el in range(len(text)):
    if text[el] == ":":
        face = text[el + 1]
        res.append(f':{face}')
print('\n'.join(res))