key = int(input())
lines = int(input())
word_list = []
for i in range(1, lines + 1):
    letters = input()
    letter = ord(letters)
    word_list.append(chr(letter + key))
print(f"{''.join(word_list)}")