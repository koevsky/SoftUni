import math
tournament_count = int(input())
initial_points = int(input())

points_gained = 0
tournament_played = 0
tournament_won = 0
for x in range(tournament_count):
    tournament_stage = input()
    if tournament_stage == "W":
        points_gained += 2000
        tournament_played += 1
        tournament_won += 1
    elif tournament_stage == "F":
        points_gained += 1200
        tournament_played += 1
    elif tournament_stage == "SF":
        points_gained += 720
        tournament_played += 1

total_points = initial_points + points_gained
average_points = points_gained / tournament_played
percent_tournaments_won = tournament_won / tournament_played * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_tournaments_won:.2f}%")
