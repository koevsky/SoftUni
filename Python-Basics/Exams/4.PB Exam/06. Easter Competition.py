import sys
easter_bread_num = int(input())

best_baker = ""
best_result = -sys.maxsize

for e in range(easter_bread_num):
    baker_name = input()
    total_points = 0
    while True:
        mark = input()
        if mark == "Stop":
            break
        mark = int(mark)
        total_points += mark
    print(f"{baker_name} has {total_points} points.")
    if total_points > best_result:
        best_result = total_points
        best_baker = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{best_baker} won competition with {best_result} points!")