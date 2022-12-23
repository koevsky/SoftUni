def chars_range(char_1, char_2):
    seq = [chr(x) for x in range(ord(char_1)+1, ord(char_2))]
    return " ".join(seq)

a, b = input(), input()
print(chars_range(a, b))