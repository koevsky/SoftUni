import re
line = input()
pattern = r"\b_([0-9A-Za-z]+)\b"
matches = re.findall(pattern, line)
print(",".join(matches))
