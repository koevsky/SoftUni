import sys
lines_count = int(input())
text = ""
is_balanced = False
for x in range(lines_count):
    text += input()

last_bracket = ""
if text.count("(") == text.count(")"):
    for y in range(len(text)):
        if text[y] == "(" and text[y] != last_bracket:
            last_bracket = text[y]
        elif last_bracket == "(" and text[y] == "(":
            is_balanced = False
            break
        elif last_bracket == "(" and text[y] == ")":
            is_balanced = True
            last_bracket = ""
else:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")