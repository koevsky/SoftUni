def dict_add(key, value, dictionary):
    dictionary = dict(dictionary)
    if key not in dictionary.keys():
        dictionary[key] = int(value)
    else:
        dictionary[key] += int(value)

    return dictionary


def stats(dictionary):
    dictionary = dict(dictionary)
    total_products = len([k for k in dictionary.keys()])
    total_qty = sum([v for v in dictionary.values()])
    res = "Products in stock:\n"
    for key, value in dictionary.items():
        res += f"- {key}: {value}\n"
    res += f"Total Products: {total_products}\nTotal Quantity: {total_qty}"

    return res


products_dict = {}
while True:
    text = input()
    if text == "statistics":
        print(stats(products_dict))
        break
    text = text.split(": ")
    k, v = text[0], text[1]
    products_dict = dict_add(k, v, products_dict)
