def grades_add(text, float_num, grades_dict):
    grades_dict = dict(grades_dict)
    if text not in grades_dict.keys():
        grades_dict[text] = [float_num]
    else:
        grades_dict[text].append(float_num)

    return grades_dict


def grades_stats(grades_dict):
    grades_dict = dict(grades_dict)
    res = ""
    for k, v in grades_dict.items():
        if (sum(v) / len(v)) >= 4.50:
            res += f"{k} -> {(sum(v) / len(v)):.2f}\n"

    return res


my_dict = {}
n = int(input())
for _ in range(n):
    name = input()
    mark = float(input())
    my_dict = grades_add(name, mark, my_dict)

print(grades_stats(my_dict))