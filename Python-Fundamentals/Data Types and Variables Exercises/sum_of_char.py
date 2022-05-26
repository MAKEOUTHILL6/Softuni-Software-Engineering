lines = int(input())
total = 0
for i in range(lines):
    letter = input()
    total += ord(letter)
print(f"The sum equals: {total}")