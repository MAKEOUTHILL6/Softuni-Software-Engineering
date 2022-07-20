text = input()
strength = 0
new_text = ''

for char in range(len(text)):
    if strength > 0 and text[char] != ">":
        strength -= 1

    elif text[char] == ">":
        strength += int(text[char + 1])
        new_text += text[char]
    else:
        new_text += text[char]

print(new_text)