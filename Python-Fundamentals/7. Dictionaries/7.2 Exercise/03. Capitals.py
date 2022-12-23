def capitals(countries, cities):
    countries = str(countries).split(", ")
    cities = str(cities).split(", ")
    my_dict = {country: city for country, city in zip(countries, cities)}
    res = ""
    for k, v in my_dict.items():
        res += f"{k} -> {v}\n"

    return res


text_1 = input()
text_2 = input()
print(capitals(text_1, text_2))