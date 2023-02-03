import os

def file_delete(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} deleted successfully")

    except:
        print('File not found')

file_delete('file_to_delete.txt')
