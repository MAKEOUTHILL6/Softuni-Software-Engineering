word = input()

word_dict = {}

for letter in word:
    if letter not in word_dict.keys() and letter != " ":
        word_dict[letter] = int(0)
    if letter != " ":
        word_dict[letter] += 1

for k, v in word_dict.items():
    print(f"{k} -> {v}")