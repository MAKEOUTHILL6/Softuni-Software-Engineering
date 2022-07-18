letters = input().split(", ")
lett = {}
for word in range(len(letters)):
    lett[letters[word]] = ord(letters[word])

print(lett)