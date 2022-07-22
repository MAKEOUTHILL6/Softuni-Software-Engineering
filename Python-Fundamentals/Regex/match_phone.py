import re
phones = input()
pattern = r"\+359(?P<separator>[\s-])2(?P=separator)\d{3}(?P=separator)\d{4}\b"
matches = re.finditer(pattern, phones)
valid_phones = [match.group() for match in matches]
print(", ".join(valid_phones))