import os


def save_extensions(dir_name, first_lvl=False):
    for filename in os.listdir(dir_name):

        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions_dict.keys():
                extensions_dict[extension] = []
            extensions_dict[extension].append(filename)

        elif os.path.isdir(file):
            save_extensions(file, first_lvl=True)


extensions_dict = {}

directory = input()

save_extensions(directory)

extensions_dict = sorted(extensions_dict.items(), key= lambda x: x[0])

result_lst = []
for extension, files in extensions_dict:
    result_lst.append(f".{extension}")

    for file in sorted(files):
        result_lst.append(f"- - -{file}")


with open("report.txt", "w") as file:
    file.write('\n'.join(result_lst))
