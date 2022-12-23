team_name = input()
games_played = int(input())
w, d, l = 0, 0, 0
points = 0
for g in range(games_played):
    result = input()
    if result == "W":
        w += 1
        points += 3
    elif result == "D":
        d += 1
        points += 1
    elif result == "L":
        l += 1

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}" )
    print(f"## L: {l}" )
    print(f"Win rate: {(w / games_played*100):.2f}%")