from collections import deque

sentence = input().split()
new_sentence = []
words = deque()
digits = ""
for word in sentence:
    for w in word:
        if w.isdigit():
            digits += w
        else:
            words.append(w)
    digits = int(digits)
    digit_char = chr(digits)
    words.appendleft(digit_char)
    new_sentence.append(words)
    words = deque()
    digits = ""
finished_list = []
for element in new_sentence:
    element[1], element[-1] = element[-1], element[1]
    finished_list.append(element)
new = ''
for el in finished_list:
    new = ''
    for e in el:
        new += e
    print(new, end=" ")