key = input().split(" ")
while True:
    line = input()
    if line == "find":
        break
    index, key_index = 0, 0
    res = ""
    while index <= len(line) - 1:
        res += chr(ord(line[index]) - int(key[key_index]))
        index += 1
        key_index += 1
        if key_index > len(key)-1:
            key_index = 0
    if "&" in res and res.count("&") == 2 and ">" in res and "<" in res:
        type_start = res.index("&")
        type_end = res.rindex("&")
        coord_start = res.index("<")
        coord_end = res.index(">")
        t_type = res[type_start+1:type_end]
        coordinates = res[coord_start+1:coord_end]
        print(f"Found {t_type} at {coordinates}")