games_sold = int(input())
hearthstone, fornite, overwatch, others = 0, 0, 0, 0
for games in range(games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1
print(f"Hearthstone - {(hearthstone/games_sold*100):.2f}%")
print(f"Fornite - {(fornite/games_sold*100):.2f}%")
print(f"Overwatch - {(overwatch/games_sold*100):.2f}%")
print(f"Others - {(others/games_sold*100):.2f}%")