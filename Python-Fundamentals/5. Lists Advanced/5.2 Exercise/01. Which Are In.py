def filtered_list(seq, subs_seq):
    filtered = []
    for x in seq:
        for y in subs_seq:
            if x in y:
                filtered.append(x)
                break
        continue
    return filtered

list_strings = input().split(", ")
list_searched = input().split(", ")

print(filtered_list(list_strings, list_searched))

