def even_text(str_list):
    str_list = [x for x in str_list if len(x) % 2 == 0]
    return str_list


strings = input().split(" ")
strings = even_text(strings)
for x in strings:
    print(x)