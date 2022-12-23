c_counter, o_counter, n_counter = 0, 0, 0
word = ""
while True:
    text = input()
    if text == "End":
        break
    if text.isalpha():
        if text == "n":
            if n_counter == 0:
                n_counter += 1
            else:
                word += text
        elif text == "o":
            if o_counter == 0:
                o_counter += 1
            else:
                word += text
        elif text == "c":
            if c_counter == 0:
                c_counter += 1
            else:
                word += text
        else:
            word += text

        if n_counter == 1 and c_counter == 1 and o_counter == 1:
            print(f"{word}",end=" ")
            word = ""
            n_counter, c_counter, o_counter = 0, 0, 0