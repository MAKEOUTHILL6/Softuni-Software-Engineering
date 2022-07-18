lines = int(input())
words_dict = {}

for _ in range(lines):
    word = input()
    synonym = input()
    if word not in words_dict:
        words_dict[word] = []
    words_dict[word].append(synonym)

for el in words_dict:
    print(f"{el} - {', '.join(words_dict[el])}")

