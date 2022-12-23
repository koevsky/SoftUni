hours = int(input())
minutes = int(input())

total_minutes = hours*60 + minutes + 15

hours = total_minutes // 60
if hours > 23:
    hours = 0
minutes = total_minutes % 60
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")

