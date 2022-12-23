import sys

n = int(input())

biggest = -sys.maxsize
smallest = sys.maxsize

for i in range(n):
    number = int(input())
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")