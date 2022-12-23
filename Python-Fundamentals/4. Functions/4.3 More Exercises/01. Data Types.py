def data_type(string, data):
    res = None
    if string == "int":
        res = int(data) * 2
    elif string == "real":
        res  = float(data) * 1.5
        res = f"{res:.2f}"
    elif string == "string":
        res = "$"+data+"$"
    return res


text, alnum = input(), input()
print(data_type(text, alnum))
