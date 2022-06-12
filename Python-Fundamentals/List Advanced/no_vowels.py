word = input()
vowels = "aoueiAOUEI"
word_filtered = list(filter(lambda x: False if x in vowels else True, word))
print(''.join(word_filtered))