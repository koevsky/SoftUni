def rep_str(string, count):
    res = string * count
    return res

text, num = input(), int(input())

print(rep_str(text, num))