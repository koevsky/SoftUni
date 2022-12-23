def course_add(text, data_dict):
    data_dict = dict(data_dict)
    text = str(text).split(" : ")
    course_name, student_name = text[0], text[1]
    if course_name not in data_dict.keys():
        data_dict[course_name] = [student_name]
    else:
        data_dict[course_name].append(student_name)

    return data_dict


def course_stats(data_dict):
    data_dict = dict(data_dict)
    res = ""
    for key, val in data_dict.items():
        res += f"{key}: {len(val)}\n"
        for name in val:
            res += f"-- {name}\n"

    return res


data_base = {}
while True:
    line = input()
    if line == "end":
        print(course_stats(data_base))
        break

    data_base = course_add(line, data_base)