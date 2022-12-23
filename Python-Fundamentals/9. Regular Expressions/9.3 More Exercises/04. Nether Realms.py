import re
demons_list = input().split(",")
demon_h_pattern = r"([^\d+\.\-\+\*\/])"
demon_d_pattern = r"((?:\+|-)?[0-9]+(?:\.[0-9]+)?)"
multidiv_pattern = r"([\*|\/])"
demons_dict = {}
for x in demons_list:
    demon = str(x).strip()
    h_search = re.findall(demon_h_pattern, demon)
    d_search = re.findall(demon_d_pattern, demon)
    signs_search = re.findall(multidiv_pattern, demon)
    if h_search:
        demon_health = sum([ord(x) for x in h_search])
    if d_search:
        demon_damage = sum([float(x) for x in d_search])
        if signs_search:
            for m in signs_search:
                if m == "*":
                    demon_damage *= 2
                elif m == "/":
                    demon_damage /= 2
    else:
        demon_damage = 0

    if demon not in demons_dict.keys():
        demons_dict[demon] = [demon_health, demon_damage]
    else:
        demons_dict[demon] = [demon_health, demon_damage]

sorted_demons_dict = dict(sorted(demons_dict.items(), key=lambda x: x[0]))
for key, val in sorted_demons_dict.items():
    print(f"{key} - {val[0]} health, {val[1]:.2f} damage")