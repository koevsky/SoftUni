num_seq = input().split(" ")
num_seq = [int(x) for x in num_seq]
left_car = (num_seq[:int(len(num_seq) / 2)])
right_car = num_seq[1 + int(len(num_seq) / 2):]
right_car.reverse()
left_car_time = 0
right_car_time = 0
for z in left_car:
    left_car_time += z
    if z == 0:
        left_car_time -= left_car_time * 20/100

for y in right_car:
    right_car_time += y
    if y == 0:
        right_car_time -= right_car_time * 20/100

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
if right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")