p_marks = {"-", ",", ".", "!", "?", "'"}

with open('text.txt', 'r') as file:
    data = [x.rstrip() for x in file.readlines()]

res_file = open('output.txt', 'w')

for l in range(len(data)):

    text = data[l]
    letters = len([m for m in text if m.isalpha()])
    symbols = len([n for n in text if n in p_marks])
    res_file.write(f"Line {l+1}: {text} ({letters})({symbols})\n")

res_file.close()

