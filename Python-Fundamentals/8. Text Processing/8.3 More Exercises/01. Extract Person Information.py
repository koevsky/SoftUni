def find_name_age(text):
    text = str(text)
    name, age = "", ""
    if "@" in text and "|" in text and "#" in text and "*" in text:
        name_start = text.index("@")
        name_end = text.index("|")
        age_start = text.index("#")
        age_end = text.index("*")
        name = text[name_start+1:name_end]
        age = text[age_start+1:age_end]
    return f"{name} is {age} years old."


n = int(input())
for _ in range(n):
    line = input()
    print(find_name_age(line))

