def file_reader(file_name):
    try:

        file = open(file_name, 'r')
        nums_sum = sum([int(x) for x in file])
        print(nums_sum)

    except FileNotFoundError:
        print('File not found')

file_reader('numbers.txt')