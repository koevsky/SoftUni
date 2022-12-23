current_record_seconds = float(input())
distance_meter = float(input())
seconds_per_meter = float(input())

slow_down_time = distance_meter // 15 * 12.5
total_time = distance_meter*seconds_per_meter + slow_down_time

if total_time < current_record_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_needed = total_time - current_record_seconds
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")