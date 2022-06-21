numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
greater_list = []

for number in numbers:
    if number > average:
        greater_list.append(number)

greater_list_sorted = sorted(greater_list, reverse=True)
final_result = greater_list_sorted[0:5]
if final_result:
    print(" ".join(str(el) for el in final_result))
else:
    print("No")