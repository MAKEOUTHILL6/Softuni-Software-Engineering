number = int(input())
for i in range(number):
    sentence = input()
    if "," in sentence or "." in sentence or "_" in sentence:
        print(f'{sentence} is not pure!')
        continue
    print(f'{sentence} is pure.')