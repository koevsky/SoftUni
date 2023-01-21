from collections import deque

green_light_duration = int(input())
free_window = int(input())

cars_passed = 0

cars_queue = deque([])
is_crash = False

while True:
    line = input()
    if line == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break

    elif line == "green":
        green_light_time = green_light_duration
        free_time = free_window
        while green_light_time and cars_queue:
            car_name = cars_queue[0]
            entered_car_length = len(cars_queue[0])
            if entered_car_length <= green_light_time:
                green_light_time -= entered_car_length
                cars_queue.popleft()
                cars_passed += 1
            elif entered_car_length > green_light_time:
                if entered_car_length <= green_light_time + free_time:
                    cars_queue.popleft()
                    green_light_time = 0
                    cars_passed += 1
                else:
                    part_hit = green_light_time + free_time
                    is_crash = True
                    print("A crash happened!")
                    print(f"{car_name} was hit at {cars_queue[0][part_hit]}.")
                    break
        if is_crash:
            break
    else:
        cars_queue.append(line)