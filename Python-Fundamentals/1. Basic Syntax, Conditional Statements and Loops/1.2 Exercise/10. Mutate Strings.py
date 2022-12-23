initial_string = input()
mutable_string = input()
previous_text = initial_string
x = 0
while True:
    transformed_text = mutable_string[:x] + initial_string[x:]
    if transformed_text == mutable_string:
        print(transformed_text)
        break
    if transformed_text != previous_text:
        print(transformed_text)
    previous_text = transformed_text
    x += 1