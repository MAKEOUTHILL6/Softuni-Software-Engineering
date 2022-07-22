import re

text = input()
word = input()
pattern = fr'\b{word}\b'
res = re.findall(pattern, text, flags=re.I)
print(len(res))