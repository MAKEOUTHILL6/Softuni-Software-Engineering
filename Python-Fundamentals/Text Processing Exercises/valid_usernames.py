import re
usernames = input().split(", ")

for ch in usernames:
    specials = '@'
    if 3 < len(ch) <= 16:
        if re.match("^[A-Za-z0-9_-]*$", ch):
            if specials not in ch:
                print(ch)