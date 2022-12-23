def stock_dict(arr):
    stock = {}
    for x in range(0, len(arr), 2):
        key = arr[x]
        val = arr[x+1]
        stock[key] = int(val)

    return stock


def available_check(dic, item):
    dic = dict(dic)
    res = ""
    if item in dic.keys():
        res = f"We have {dic[item]} of {item} left"
    else:
        res = f"Sorry, we don't have {item}"

    return res


stock = input().split(" ")
product_list = input().split(" ")

for product in product_list:
    print(available_check(stock_dict(stock), product))