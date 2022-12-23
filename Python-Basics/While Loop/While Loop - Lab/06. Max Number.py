import sys
max_num = -sys.maxsize
while True:
    data = input()
    if data == "Stop":
        break
    data = int(data)
    if data > max_num:
        max_num = data

print(max_num)