def double(word):
    while word != "End":
        if word == "SoftUni":
            word = input()
            continue
        for ch in word:
            new_word = ch * 2
            print(new_word, end="")
        print()
        word = input()


word = input()
double(word)