def vowel_remove(string):

    string = [x for x in string if x.lower() not in "aeoui"]
    string = "".join(string)
    return string


text = input()
print(vowel_remove(text))