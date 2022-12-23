import re
line = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, line)
destinations = [x[1] for x in matches]
points = sum(len(x[1]) for x in matches)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")

