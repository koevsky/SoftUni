import math
series_name = input()
episode_duration = int(input())
break_duration = int(input())

launch_duration = break_duration / 8
rest_duration = break_duration / 4

total_time = launch_duration + rest_duration + episode_duration

if break_duration >= total_time:
    time_left = break_duration - total_time
    time_left = math.ceil(time_left)
    print(f"You have enough time to watch {series_name} and left with {time_left} minutes free time.")
else:
    time_needed = total_time - break_duration
    time_needed = math.ceil(time_needed)
    print(f"You don't have enough time to watch {series_name}, you need {time_needed} more minutes.")