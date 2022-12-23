def merge(str_seq, s, e):
    s, e = int(s), int(e)
    str_seq = list(str_seq)
    if 0 <= s < e <= len(str_seq) - 1:      # In range
        joined_elements = [str_seq[x] for x in range(s, e+1)]
        str_seq = str_seq[:s] + ["".join(joined_elements)] + str_seq[e+1:]

    elif 0 > s < e <= len(str_seq) - 1:     # Left side out
        joined_elements = [str_seq[x] for x in range(0, e+1)]
        str_seq = ["".join(joined_elements)] + str_seq[e+1:]

    elif 0 <= s <= (len(str_seq) - 1) < e:  # Right side out
        joined_elements = [str_seq[x] for x in range(s, len(str_seq))]
        str_seq = str_seq[:s] + ["".join(joined_elements)]

    elif 0 > s < e > len(str_seq) - 1:      # Both sides out
        joined_elements = ["".join(str_seq)]
        str_seq = joined_elements

    return str_seq


def divide(str_seq, i, p):
    i, p = int(i), int(p)
    str_seq = list(str_seq)
    if len(str_seq[i]) % p == 0:    # Equal partitions
        step = int(len(str_seq[i])/p)
        divided_element = [str_seq[i][x:x+step] for x in range(0, len(str_seq[i]), step)]
        str_seq = str_seq = str_seq[:i] + divided_element + str_seq[i+1:]
    elif len(str_seq[i]) % p != 0:     # Not equal partitions
        step = int(len(str_seq[i]) // p)
        divided_element = []
        parts_counter = 0
        for x in range(0, len(str_seq[i]), step):
            if parts_counter != p - 1:
                divided_element.append(str_seq[i][x:x + step])
                parts_counter += 1
            else:
                divided_element.append(str_seq[i][(p - 1) * step:])
                break
        str_seq = str_seq[:i] + divided_element + str_seq[i+1:]

    return str_seq


data_array = input().split(" ")
while True:
    command = input()
    if command == "3:1":
        print(" ".join(data_array))
        break
    command = command.split(" ")
    if "merge" in command:
        start = command[1]
        end = command[2]
        data_array = merge(data_array, start, end)
    elif "divide" in command:
        index = command[1]
        partitions = command[2]
        data_array = divide(data_array, index, partitions)