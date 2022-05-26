word = input()
list_str = []
for letter in range(len(word)):
    if word[letter].isupper():
        list_str.append(letter)
print(list_str)