def sum_beach(sentence):
    words = ["sand", "fish", "water", "sun"]
    count = 0
    for word in words:
        if word in sentence:
            word_count = sentence.count(word)
            count += word_count
    print(count)


sentence = input().lower()
sum_beach(sentence)