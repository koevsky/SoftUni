actor_name = input()
points = float(input())
jury_count = int(input())
threshold = 1250.5
for people in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    points += len(jury_name) * jury_points / 2
    if points >= threshold:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
if points < threshold:
    points_need = threshold - points
    print(f"Sorry, {actor_name} you need {points_need:.1f} more!")