result_list = [input().split(" ") for x in range(3)]
is_player_one = False
is_player_two = False
if result_list[0].count("1") == 3 or result_list[1].count("1") == 3 or result_list[2].count("1") == 3:
    is_player_one = True
elif result_list[0].count("2") == 3 or result_list[1].count("2") == 3 or result_list[2].count("2") == 3:
    is_player_two = True

for x in range(3):
    if result_list[0][x] == "1" and result_list[1][x] == "1" and result_list[2][x] == "1":
        is_player_one = True
    elif result_list[0][x] == "2" and result_list[1][x] == "2" and result_list[2][x] == "2":
        is_player_two = True

if result_list[0][0] == "1" and result_list[1][1] == "1" and result_list[2][2] == "1":
    is_player_one = True
elif result_list[0][0] == "2" and result_list[1][1] == "2" and result_list[2][2] == "2":
    is_player_two = True

if result_list[0][2] == "1" and result_list[1][1] == "1" and result_list[2][0] == "1":
    is_player_one = True
elif result_list[0][2] == "2" and result_list[1][1] == "2" and result_list[2][0] == "2":
    is_player_two = True

if is_player_one:
    print("First player won")
elif is_player_two:
    print("Second player won")
else:
    print("Draw!")