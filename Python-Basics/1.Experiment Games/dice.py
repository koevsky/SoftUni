from random import randrange

while True:
    data = input()
    if data == " ":
        dice_one = randrange(1, 7)
        dice_two = randrange(1, 7)
        print(dice_one)
        print(dice_two)

