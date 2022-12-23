start, finish, exception = input(), input(), input()
valid_combinations = 0

for first in range(ord(start), ord(finish) + 1):
    for second in range(ord(start), ord(finish) + 1):
        for third in range(ord(start), ord(finish) + 1):
            message = chr(first) + chr(second) + chr(third)
            if exception not in message:
                print(message, end=" ")
                valid_combinations += 1
print(valid_combinations)