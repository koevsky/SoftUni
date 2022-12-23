name = input()
password = input()

while True:
    new_pass = input()
    if new_pass == password:
        break

print(f"Welcome {name}!")