def sorting_cheeses(**kwargs):

    sorted_cheeses = sorted(kwargs.items(), key= lambda x: (-len(x[1]), x[0]))

    res = ""
    for key, val in sorted_cheeses:
        res += f"{key}\n"
        for x in sorted(val, reverse= True):
            res += f"{x}\n"

    return res

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

