word = input()
second_word = input()

while word in second_word:
    second_word = second_word.replace(word, '')
print(second_word)