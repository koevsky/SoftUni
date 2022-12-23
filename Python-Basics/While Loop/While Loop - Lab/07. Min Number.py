import sys
min_num = sys.maxsize
while True:
    data = input()
    if data == "Stop":
        break
    data = int(data)
    if data < min_num:
        min_num = data

print(min_num)