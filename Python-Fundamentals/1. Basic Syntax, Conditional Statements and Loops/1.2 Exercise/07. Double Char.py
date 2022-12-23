while True:
    text = input()
    if text == "End":
        break
    elif text == "SoftUni":
        continue
    print("".join([x * 2 for x in text]))