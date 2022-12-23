line = input().split()
total = 0
for string in line:
    num = int("".join([x for x in string if x.isdigit()]))
    start_letter = string[0]
    end_letter = string[-1]
    if start_letter.isupper():
        letter_pos = 26 - (90 - ord(start_letter))
        num /= letter_pos
    elif start_letter.islower():
        letter_pos = 26 - (122 - ord(start_letter))
        num *= letter_pos

    if end_letter.isupper():
        letter_pos = 26 - (90 - ord(end_letter))
        num -= letter_pos
    elif end_letter.islower():
        letter_pos = 26 - (122 - ord(end_letter))
        num += letter_pos
    total += num

print(f"{total:.2f}")