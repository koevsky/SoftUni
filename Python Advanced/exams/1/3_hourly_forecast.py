def forecast(*args):

    res_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for info in args:
        city, weather = info
        res_dict[weather].append(city)

    res = []

    for key, val in res_dict.items():
        if val:
            for ct in sorted(val):
                res.append(f"{ct} - {key}")

    return "\n".join(res)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))





