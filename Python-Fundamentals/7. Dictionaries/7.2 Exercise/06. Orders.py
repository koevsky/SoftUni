def product_add(text, product_dict):
    product_dict = dict(product_dict)
    text = str(text).split(" ")
    name, price, qty = text[0], float(text[1]), int(text[2])
    if name not in product_dict.keys():
        product_dict[name] = [price, qty]
    else:
        product_dict[name][1] += qty
        if product_dict[name][0] != price:
            product_dict[name][0] = price

    return product_dict


def product_stats(product_dict):
    product_dict = dict(product_dict)
    res = ""
    for k, v in product_dict.items():
        res += f"{k} -> {(v[0] * v[1]):.2f}\n"

    return res


products = {}
while True:
    line = input()
    if line == "buy":
        print(product_stats(products))
        break

    products = product_add(line, products)