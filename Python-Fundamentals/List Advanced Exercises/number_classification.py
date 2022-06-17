numbers = list(map(int, input().split(", ")))

positives = [el for el in numbers if el >= 0]
negatives = [el for el in numbers if el < 0]
even = [el for el in numbers if el % 2 == 0]
odd = [el for el in numbers if el % 2 != 0]

print(f"Positive: {', '.join(str(el) for el in positives)}")
print(f"Negative: {', '.join(str(el) for el in negatives)}")
print(f"Even: {', '.join(str(el) for el in even)}")
print(f"Odd: {', '.join(str(el) for el in odd)}")