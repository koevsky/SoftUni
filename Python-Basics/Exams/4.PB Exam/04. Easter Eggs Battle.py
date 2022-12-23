first_player_eggs, second_player_eggs = int(input()), int(input())

while True:
    text = input()
    if text == "End":
        print(f"Player one has {first_player_eggs} eggs left.")
        print(f"Player two has {second_player_eggs} eggs left.")
        break
    if text == "one":
        second_player_eggs -= 1
        if second_player_eggs == 0:
            print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
            break
    elif text == "two":
        first_player_eggs -= 1
        if first_player_eggs == 0:
            print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
            break
