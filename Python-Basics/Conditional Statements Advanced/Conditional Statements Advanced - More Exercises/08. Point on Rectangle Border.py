x1= float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

x = float(input())
y = float(input())

condition = ""
if x1 <= x <= x2 and (y == y1 or y == y2):
    condition = "Border"
else:
    condition = "Inside / Outside"
if y1 <= y <= y2 and (x == x1 or x == x2):
    condition = "Border"
else:
    "Inside / Outside"
print(condition)


