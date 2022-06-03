team_a = []
team_b = []

game_terminated = False

for player in range(1, 12):
    team_a.append(f"A-{player}")
    team_b.append(f"B-{player}")

card = input().split()

for player in card:
    if player in team_a:
        team_a.remove(player)
    if player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_terminated:
    print("Game was terminated")
