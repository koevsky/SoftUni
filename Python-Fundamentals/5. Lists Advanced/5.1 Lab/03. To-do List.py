def list_arrange(seq, num, txt):
    num = int(num)
    seq[num-1] = txt
    return seq


to_do = [0]*10
while True:
    text = input()
    if text == "End":
        while 0 in to_do:
            to_do.remove(0)
        print(to_do)
        break
    text = text.split("-")
    importance = text[0]
    string = text[1]
    to_do = list_arrange(to_do, importance, string)