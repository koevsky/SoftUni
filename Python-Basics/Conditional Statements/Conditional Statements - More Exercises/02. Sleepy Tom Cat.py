resting_days = int(input())
working_days = 365 - resting_days

working_days_playtime = working_days * 63
resting_days_playtime = resting_days * 127

total_playtime = working_days_playtime + resting_days_playtime

if total_playtime > 30000:
    time_more = total_playtime - 30000
    hours = time_more // 60
    minutes = time_more % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    time_less = 30000 - total_playtime
    hours = time_less // 60
    minutes = time_less % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")