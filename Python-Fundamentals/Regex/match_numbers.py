import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
res = re.finditer(pattern, text)
for match in res:
    print(match.group(), end=" ")