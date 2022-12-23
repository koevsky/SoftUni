def decipher(str_list):
    message = []
    str_list = [str(w) for w in str_list]
    for word in str_list:
        letters = [l for l in word if l.isalpha()]
        digits = [d for d in word if d. isdigit()]
        letters[0], letters[-1] = letters[-1], letters[0]
        deciphered = "".join(chr(int("".join(digits)))) + "".join(letters)
        message.append(deciphered)
    return " ".join(message)


words = input().split(" ")
print(decipher(words))

