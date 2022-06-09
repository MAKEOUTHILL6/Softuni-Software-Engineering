numbers = input().split()
left_car = []
right_car = []
sum_left = 0
sum_right = 0
for nums in numbers:
    middle = len(numbers) // 2
    left_car = numbers[0:middle]
    right_car = numbers[middle + 1::]
left_side_as_digits = list(map(int, left_car))
right_side_as_digits = reversed(list(map(int, right_car)))
for number in left_side_as_digits:
    sum_left += number
    if number == 0:
        sum_left *= 0.8
for nam in right_side_as_digits:
    sum_right += nam
    if nam == 0:
        sum_right *= 0.8
if sum_left < sum_right:
    print(f"The winner is left with total time: {sum_left:.1f}")
else:
    print(f"The winner is right with total time: {sum_right:.1f}")