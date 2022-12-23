import re

pattern = "(^|(?<=\s))(www\.([a-zA-Z0-9]+\-?[a-zA-Z0-9]+)+\.([a-z]+\.?[a-z]+)+)($|(?=\s))"

while True:
    line = input()
    if line:
        searched = re.finditer(pattern, line)
        for x in searched:
            print(x.group())
    else:
        break