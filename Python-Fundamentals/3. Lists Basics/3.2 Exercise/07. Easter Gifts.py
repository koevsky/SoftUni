planed_gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    command = command.split(" ")
    if "OutOfStock" in command:
        gift = command[1]
        while gift in planed_gifts:
            ind = planed_gifts.index(gift)
            planed_gifts[ind] = "None"
    elif "Required" in command:
        gift, index = command[1], int(command[2])
        if 0 <= index <= len(planed_gifts) - 1:
            planed_gifts[index] = gift
    elif "JustInCase" in command:
        gift = command[1]
        planed_gifts[-1] = gift
while "None" in planed_gifts:
    planed_gifts.remove("None")

print(" ".join(planed_gifts))