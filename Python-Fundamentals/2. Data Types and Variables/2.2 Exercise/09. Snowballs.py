import sys
snowball_count = int(input())
best_value = -sys.maxsize
best_weight, best_time, best_quality = None, None, None
for sb in range(snowball_count):
    sb_weight = int(input())
    sb_time = int(input())
    sb_quality = int(input())
    sb_value = (sb_weight / sb_time) ** sb_quality
    if sb_value > best_value:
        best_value = sb_value
        best_time = sb_time
        best_weight = sb_weight
        best_quality = sb_quality
print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")
