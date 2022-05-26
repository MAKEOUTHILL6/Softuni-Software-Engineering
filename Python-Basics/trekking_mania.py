groups = int(input())

all_people = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for trekkers in range(1, groups + 1):
    number_of_trekkers = int(input())
    if number_of_trekkers <= 5:
        musala += number_of_trekkers
    elif 6 <= number_of_trekkers <= 12:
        monblan += number_of_trekkers
    elif 13 <= number_of_trekkers <= 25:
        kilimanjaro += number_of_trekkers
    elif 26 <= number_of_trekkers <= 40:
        k2 += number_of_trekkers
    elif number_of_trekkers >= 41:
        everest += number_of_trekkers
all_people = musala + monblan + kilimanjaro + k2 + everest
print(f"{musala / all_people * 100:.2f}%")
print(f"{monblan / all_people * 100:.2f}%")
print(f"{kilimanjaro / all_people * 100:.2f}%")
print(f"{k2 / all_people * 100:.2f}%")
print(f"{everest / all_people * 100:.2f}%")
