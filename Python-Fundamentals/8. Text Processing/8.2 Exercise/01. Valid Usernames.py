text = input().split(", ")


def word_filter(word):
    word = str(word)
    if 3 <= len(word) <= 16:
        res = True
        for x in word:
            if x.isalnum() or x == "_" or x == "-":
                res = True
            else:
                res = False
                break
        return res


text = filter(word_filter, text)
for x in text:
    print(x)



