def file_opener(file_name):
    try:
        file = open(file_name, 'r')
        print('File found')

    except FileNotFoundError:
        print('File not found')

file_opener('my_first_file.txt')