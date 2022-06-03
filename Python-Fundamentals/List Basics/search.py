def search(lines, word):
    all_list = []
    word_list = []
    for i in range(lines):
        sentences = input()
        all_list.append(sentences)
        if word in sentences:
            word_list.append(sentences)

    print(all_list)
    print(word_list)


lines = int(input())
word = input()
search(lines, word)