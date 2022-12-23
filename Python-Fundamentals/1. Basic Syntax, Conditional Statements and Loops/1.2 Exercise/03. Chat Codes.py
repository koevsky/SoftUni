n = int(input())
for i in range(n):
    num = int(input())
    if num > 88:
        print("Bye.")
    elif num < 88 and num != 86:
        print("GREAT!")
    elif num == 86:
        print("How are you?")
    elif num == 88:
        print("Hello")