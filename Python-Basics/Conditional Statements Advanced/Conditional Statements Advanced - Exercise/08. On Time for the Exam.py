exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

total_exam_minutes = exam_hour * 60 + exam_minute
total_arrival_minutes = arrival_hour * 60 + arrival_minute

state = ""
if total_arrival_minutes <= total_exam_minutes: # On time / Early
    difference = total_exam_minutes - total_arrival_minutes
    if difference <= 30 and difference != 0:
        state = "On time"
        print(state)
        print(f"{difference} minutes before the start")
    elif difference == 0:
        state = "On time"
        print(state)
    else:
        state = "Early"
        print(state)
        if difference > 59:
            hours = difference // 60
            minutes = difference % 60
            if minutes < 10:
                print(f"{hours}:0{minutes} hours before the start")
            else:
                print(f"{hours}:{minutes} hours before the start")
        else:
            print(f"{difference} minutes before the start")
else:
    difference = total_arrival_minutes - total_exam_minutes
    state = "Late"
    print(state)
    if difference > 59:
        hours = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
    else:
        print(f"{difference} minutes after the start")
