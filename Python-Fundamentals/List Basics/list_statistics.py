lines = int(input())

positive_list = []
negative_list = []

for i in range(lines):
    numbers = int(input())
    if numbers >= 0:
        positive_list.append(numbers)
    else:
        negative_list.append(numbers)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
