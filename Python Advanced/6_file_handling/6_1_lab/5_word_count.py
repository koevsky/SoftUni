with open('words.txt', 'r') as words_file:
    searched_words = {word.lower(): 0 for word in words_file.readline().split()}

with open('text.txt', 'r') as text_file:
    lines = [line.rstrip().lower().split() for line in text_file]
    words = []
    [words.extend(x) for x in lines]
    words = [x.strip("-,!?.",) for x in words]

[print(f"{w} - {words.count(w)}") for w in searched_words.keys()]




