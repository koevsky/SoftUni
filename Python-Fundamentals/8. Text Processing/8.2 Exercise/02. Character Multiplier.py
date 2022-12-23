strings = input().split(" ")
longer_word_list = list(sorted(strings, key=lambda x: len(x), reverse=True))
word_1, word_2 = longer_word_list[0], longer_word_list[1]
total_res = 0
index = 0
while index <= len(word_1) - 1:
    if index <= len(word_2) - 1:
        total_res += ord(word_1[index]) * ord(word_2[index])
    else:
        total_res += ord(word_1[index])
    index += 1
print(total_res)



