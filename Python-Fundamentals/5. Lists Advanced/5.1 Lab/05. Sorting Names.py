def sort_names(seq):
    seq = list(seq)
    seq.sort()
    seq.sort(key=len, reverse=True)
    return seq


names = input().split(", ")
print(sort_names(names))