def file_writer(text_in_file):
    new_file = open('new_file.txt', 'w')
    new_file.write(text_in_file)
    print('New file created')

file_writer('I just created my first file!')