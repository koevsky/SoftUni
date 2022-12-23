def decipher(str_list):
    res = ""
    str_list = list(str_list)
    num_list = [int(x) for x in str_list if str(x).isdigit()]
    str_list = [x for x in str_list if not str(x).isdigit()]
    last_index = 0
    for x in range(len(num_list)):
        if x % 2 == 0:
            take_count = num_list[x]
            if take_count > 0:
                res += "".join(str_list[last_index:take_count+last_index])
                last_index += take_count
        else:
            skip_count = num_list[x]
            last_index += skip_count
    return res


string = input()
print(decipher(string))