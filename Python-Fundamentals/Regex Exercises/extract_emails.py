import re
pattern = r"((?<=\s)([a-z0-9]+[-\.\_a-z0-9]*)@([a-z]+)(-[a-z]+)*\.([a-z\.]+))\b"
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())