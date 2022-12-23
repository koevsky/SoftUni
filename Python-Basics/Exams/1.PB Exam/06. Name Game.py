best_result = 0
best_player = ""
while True:
    name = input()
    if name == "Stop":
        break
    points = 0
    for char in name:
        digit = int(input())
        if ord(char) == digit:
            points += 10
        else:
            points += 2
    if points >= best_result:
        best_player = name
        best_result = points
print(f"The winner is {best_player} with {best_result} points!")

