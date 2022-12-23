import re

pattern = r"(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b"
line = input()
result = re.findall(pattern, line)
print(", ".join(result))