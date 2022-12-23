import math
tries = int(input())
points, red_count, orange_count, yellow_count, white_count, black_count, others_count = 0, 0, 0, 0, 0, 0, 0
for i in range(tries):
    color = input()
    if color == "red":
        points += 5
        red_count += 1
    elif color == "orange":
        points += 10
        orange_count += 1
    elif color == "yellow":
        points += 15
        yellow_count += 1
    elif color == "white":
        points += 20
        white_count += 1
    elif color == "black":
        points /= 2
        points = math.floor(points)
        black_count += 1
    else:
        others_count += 1
        pass
print(f"Total points: {points}")
print(f"Red balls: {red_count}")
print(f"Orange balls: {orange_count}")
print(f"Yellow balls: {yellow_count}")
print(f"White balls: {white_count}")
print(f"Other colors picked: {others_count}")
print(f"Divides from black balls: {black_count}")