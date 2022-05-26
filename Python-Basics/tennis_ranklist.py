tournaments = int(input())
starter_points = int(input())

W = 0
F = 0
SF = 0
total_points = 0
total_wins = 0
average_points = 0
percent_won = 0

for i in range(tournaments):
    position = input()
    if position == "W":
        W += 2000
        total_wins += 1
    elif position == "F":
        F += 1200
    elif position == "SF":
        SF += 720
    total_points = W + F + SF + starter_points
    average_points = (W + F + SF) // tournaments
    percent_won = (total_wins / tournaments) * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")