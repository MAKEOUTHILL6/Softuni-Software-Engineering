word_start = input()
word_end = input()
invalid_word = input()

count = 0

for i in range(ord(word_start), ord(word_end) + 1):
    for j in range(ord(word_start), ord(word_end) + 1):
        for k in range(ord(word_start), ord(word_end) + 1):
            if ord(invalid_word) != i and ord(invalid_word) != j and ord(invalid_word) != k:
                count += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}")
print(count)
