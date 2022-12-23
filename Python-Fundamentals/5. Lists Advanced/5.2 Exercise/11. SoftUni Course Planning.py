def add(str_list, text):
    str_list = list(str_list)
    if text not in str_list:
        str_list.append(text)
    return str_list


def insert(str_list, text, i):
    str_list = list(str_list)
    i = int(i)
    if text not in str_list:
        str_list.insert(i, text)
    return str_list


def remove(str_list, text):
    str_list = list(str_list)
    if text in str_list:
        while text in str_list:
            str_list.remove(text)
    if text+"-Exercise" in str_list:
        while text+"-Exercise" in str_list:
            str_list.remove(text+"-Exercise")
    return str_list


def swap(str_list, text_1, text_2):
    str_list = list(str_list)
    if (text_1 in str_list) and (text_2 in str_list):
        i_text_1 = str_list.index(text_1)
        i_text_2 = str_list.index(text_2)
        str_list[i_text_1], str_list[i_text_2] = str_list[i_text_2], str_list[i_text_1]
        if (text_1+"-Exercise" in str_list) and (text_2+"-Exercise" in str_list):
            str_list[i_text_1+1], str_list[i_text_2+1] = str_list[i_text_2+1], str_list[i_text_1+1]
        elif text_1+"-Exercise" in str_list and text_2+"-Exercise" not in str_list:
            i_text_1 = str_list.index(text_1)
            str_list.remove(text_1+"-Exercise")
            str_list.insert(i_text_1+1, text_1+"-Exercise")
        elif text_2+"-Exercise" in str_list and text_1+"-Exercise" not in str_list:
            i_text_2 = str_list.index(text_2)
            str_list.remove(text_2+"-Exercise")
            str_list.insert(i_text_2+1, text_2+"-Exercise")

    return str_list


def exercise(str_list, text):
    str_list = list(str_list)
    if text in str_list:
        if text+"-Exercise" not in str_list:
            lesson_index = str_list.index(text)
            str_list.insert(lesson_index+1, text+"-Exercise")
    else:
        str_list.append(text)
        str_list.append(text+"-Exercise")
    return str_list


string_list = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    command = command.split(":")
    if "Add" in command:
        lesson_title = command[1]
        string_list = add(string_list, lesson_title)
    elif "Insert" in command:
        lesson_title = command[1]
        index = command[2]
        string_list = insert(string_list, lesson_title, index)
    elif "Remove" in command:
        lesson_title = command[1]
        string_list = remove(string_list, lesson_title)
    elif "Swap" in command:
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        string_list = swap(string_list, lesson_title_1, lesson_title_2)
    elif "Exercise" in command:
        lesson_title = command[1]
        string_list = exercise(string_list, lesson_title)

for x in range(len(string_list)):
    print(f"{x+1}.{string_list[x]}")
