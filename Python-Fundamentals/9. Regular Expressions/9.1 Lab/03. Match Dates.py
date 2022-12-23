import re
line = input()

pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"

res = re.findall(pattern, line)

for x in res:
    print(f"Day: {x[0]}, Month: {x[2]}, Year: {x[3]}")
