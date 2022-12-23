counter = 0
while True:
    text = input()
    if text == "END":
        print(counter)
        break
    if text == text.upper():
        text = text.lower()
        if text == "coding" or text == "dog" or text == "cat" or text == "movie":
            counter += 2
    elif text == "coding" or text == "dog" or text == "cat" or text == "movie":
        counter += 1

    if counter > 5:
        print("You need extra sleep")
        break