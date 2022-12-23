def bakery_dict(arr):
    bakery = {}
    for x in range(0, len(arr), 2):
        key = arr[x]
        val = arr[x+1]
        bakery[key] = int(val)

    return bakery


elements = input().split(" ")
print(bakery_dict(elements))
