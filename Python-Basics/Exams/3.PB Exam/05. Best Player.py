import sys
best_player_score = -sys.maxsize
best_player_name = ""

while True:
    text = input()
    if text == "END":
        break
    goals = int(input())
    if goals > best_player_score:
        best_player_score = goals
        best_player_name = text
    if goals >= 10:
        break
print(f"{best_player_name} is the best player!")
if 3 <= best_player_score:
    print(f"He has scored {best_player_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_score} goals.")