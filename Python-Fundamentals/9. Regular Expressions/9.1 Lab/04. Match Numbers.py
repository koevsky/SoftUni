import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
line = input()
result = re.finditer(pattern, line)
for obj in result:
    print(obj.group(), end=" ")
