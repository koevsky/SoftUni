def ascii_dict(text):
    text = str(text).split(", ")
    my_dict = {str(x): ord(x) for x in text}

    return my_dict


line = input()
print(ascii_dict(line))
