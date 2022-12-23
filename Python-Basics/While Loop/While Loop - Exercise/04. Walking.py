steps_walked = 0

while True:
    data = input()
    if data == "Going home":
        steps_to_home = int(input())
        steps_walked += steps_to_home
        break
    else:
        data = int(data)
        steps_walked += data
    if steps_walked >= 10000:
        break

if steps_walked < 10000:
    print(f"{10000 - steps_walked} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps_walked - 10000} steps over the goal!")