import random, time

options = ["rock", "paper", "scissors"]
print()
print("                 --->THIS IS A GAME OF ROCK, PAPER AND SCISSORS AGAINST THE ULTIMATE MACHINE... GOOD LUCK<---")
print()
player_name = input("Please input player name here ---> ")
print(f"{player_name} BE READY FOR BATTLE ! SELECT YOUR WEAPON -> (rock->(r) , paper->(p), scissors->(s), quit)")
print()
rounds_draw, rounds_won, rounds_lost, battles_won, battles_lost, battles_draw, total_battles = 0, 0, 0, 0, 0, 0, 0

while True:
    data = input("Enter your choice (r, p, s) here --> ")
    if data == "quit":
        total_rounds = rounds_lost + rounds_draw + rounds_won
        print()
        print("    ----->FINAL STATS<------")
        time.sleep(2)
        bar1 = int(rounds_won / total_rounds*10)*'#' + ((10-int(rounds_won / total_rounds*10))*".")
        print(f"WIN RATIO: [{bar1}] {(rounds_won / total_rounds*100):.2f}%")
        print("------------------------------")
        time.sleep(2)
        bar2 = int(rounds_draw / total_rounds*10)*'#' + ((10-int(rounds_draw / total_rounds*10))*".")
        print(f"DRAW RATIO: [{bar2}] {(rounds_draw / total_rounds * 100):.2f}%")
        print("------------------------------")
        time.sleep(2)
        bar3 = int(rounds_lost / total_rounds*10)*'#' + ((10-int(rounds_lost / total_rounds*10))*".")
        print(f"LOSE RATIO: [{bar3}] {(rounds_lost / total_rounds * 100):.2f}%")
        print("------------------------------")
        break

    pc_choice = random.choice(options)
    if data == "r":
        if pc_choice == options[2]:
            print(f"Your choice: {options[0]}")
            print(f"Opponent choice: {pc_choice}")
            print("You WON a battle !!!")
            print()
            battles_won += 1
        elif pc_choice == options[0]:
            print(f"Your choice: {options[0]}")
            print(f"Opponent choice: {pc_choice}")
            print("Draw !")
            print()
            battles_draw += 1
        elif pc_choice == options[1]:
            print(f"Your choice: {options[0]}")
            print(f"Opponent choice: {pc_choice}")
            print("You LOST a battle :(")
            print()
            battles_lost += 1
        total_battles += 1

    elif data == "p":
        if pc_choice == options[0]:
            print(f"Your choice: {options[1]}")
            print(f"Opponent choice: {pc_choice}")
            print("You WON a battle !!!")
            print()
            battles_won += 1
        elif pc_choice == options[1]:
            print(f"Your choice: {options[1]}")
            print(f"Opponent choice: {pc_choice}")
            print("Draw !")
            print()
            battles_draw += 1
        elif pc_choice == options[2]:
            print(f"Your choice: {options[1]}")
            print(f"Opponent choice: {pc_choice}")
            print("You LOST a battle :(")
            print()
            battles_lost += 1
        total_battles += 1

    elif data == "s":
        if pc_choice == options[1]:
            print(f"Your choice: {options[2]}")
            print(f"Opponent choice: {pc_choice}")
            print("You WON a battle !!!")
            print()
            battles_won += 1
        elif pc_choice == options[2]:
            print(f"Your choice: {options[2]}")
            print(f"Opponent choice: {pc_choice}")
            print("Draw !")
            print()
            battles_draw += 1
        elif pc_choice == options[0]:
            print(f"Your choice: {options[2]}")
            print(f"Opponent choice: {pc_choice}")
            print("You LOST a battle :(")
            print()
            battles_lost += 1
        total_battles += 1
    else:
        print("WRONG INPUT ! TRY AGAIN !(r, p, s, quit)")
        print()

    if total_battles % 3 == 0:
        if battles_won >= 2 or (battles_draw == 2 and battles_won == 1):
            print("!!! ROUND WON !!!")
            print()
            rounds_won += 1
        elif battles_draw == 3 or (battles_lost == 1 and battles_won == 1 and battles_draw == 1):
            print(">>ROUND DRAW<<")
            print()
            rounds_draw += 1
        elif battles_lost >= 2 or (battles_draw == 2 and battles_lost == 1):
            print("...ROUND LOST... ")
            print()
            rounds_lost += 1
        battles_lost, battles_draw, battles_won = 0, 0, 0