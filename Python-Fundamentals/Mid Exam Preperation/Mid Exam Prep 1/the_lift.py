people = int(input())
current_wagons = list(map(int, input().split()))

for i in range(len(current_wagons)):
    max_people = min(4 - current_wagons[i], people)
    current_wagons[i] += max_people
    people -= max_people


if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif len([wagon for wagon in current_wagons if wagon < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(wagon) for wagon in current_wagons]))