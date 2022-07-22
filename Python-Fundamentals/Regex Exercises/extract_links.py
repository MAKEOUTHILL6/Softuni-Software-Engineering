import re

pattern = r'(www\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))'
text = input()
while True:
    matches = re.finditer(pattern, text)
    if text:
        if matches:
            for match in matches:
                print(match.group())
        text = input()
    else:
        break