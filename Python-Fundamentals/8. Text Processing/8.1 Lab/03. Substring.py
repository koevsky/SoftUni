word_1, word_2 = input(), input()
while word_1 in word_2:
    word_2 = word_2.replace(word_1, "")
print(word_2)