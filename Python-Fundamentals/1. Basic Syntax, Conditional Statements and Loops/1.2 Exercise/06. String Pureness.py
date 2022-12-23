n = int(input())
for x in range(n):
    text = input()
    if "_" not in text and "." not in text and "," not in text:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")