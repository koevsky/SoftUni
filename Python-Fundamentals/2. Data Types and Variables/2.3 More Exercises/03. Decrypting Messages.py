key, letter_count = int(input()), int(input())
print("".join([chr(ord(input()) + key) for x in range(letter_count)]))
