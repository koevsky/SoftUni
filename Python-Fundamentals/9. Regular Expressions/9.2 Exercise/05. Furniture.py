import re
pattern = r"(^|(?<=\s))>>([a-zA-Z]+)<<([0]|[1-9][0-9]*)(\.\d+)?!([0]|[1-9][0-9]*)($|(?=\s))"
total_price = 0
furniture_list = []
while True:
    line = input()
    if line == "Purchase":
        break
    searched = re.findall(pattern, line)
    if searched:
        furniture_list.append(searched[0][1])
        if searched[0][3]:
            total_price += float(searched[0][2]+searched[0][3]) * int(searched[0][4])
        else:
            total_price += int(searched[0][2]) * int(searched[0][4])

print("Bought furniture:")
for item in furniture_list:
    print(item)
print(f"Total money spend: {total_price:.2f}")