player_1, player_2 = input().split(", ")

current = player_1
other = player_2

board = [input().split() for x in range(6)]

while True:

    row, col = [int(x) for x in input().strip('()').split(", ")]
    if current[-1] != "W":
        if board[row][col] == "E":
            print(f"{current} found the Exit and wins the game!")
            break

        elif board[row][col] == "T":
            print(f"{current} is out of the game! The winner is {other}.")
            break

        elif board[row][col] == "W":
            print(f"{current} hits a wall and needs to rest.")
            current += "W"
    else:
        current = current.replace("W", "")

    current, other = other, current





