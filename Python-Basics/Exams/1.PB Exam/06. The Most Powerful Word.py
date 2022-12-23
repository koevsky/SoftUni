import math
most_powerful = 0
the_word = ""
while True:
    word = input()
    if word == "End of words":
        break
    points = 0
    for char in word:
        points += ord(char)
    if word[0].lower() in "aeiouy":
        points *= len(word)
    else:
        points /= len(word)
        points = math.floor(points)
    if points > most_powerful:
        the_word = word
        most_powerful = points
print(f"The most powerful word is {the_word} - {most_powerful}" )

