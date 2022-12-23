def add(dictionary, piece, composer, key):
    dictionary = dict(dictionary)
    if piece not in dictionary.keys():
        dictionary[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return dictionary


def remove(dictionary, piece):
    dictionary = dict(dictionary)
    if piece in dictionary.keys():
        print(f"Successfully removed {piece}!")
        dictionary.pop(piece, None)
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return dictionary


def change_key(dictionary, piece, new_kew):
    dictionary = dict(dictionary)
    if piece in dictionary.keys():
        print(f"Changed the key of {piece} to {new_kew}!")
        dictionary[piece][1] = new_kew
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return dictionary


collection_dict = {}
num = int(input())
for x in range(num):
    line = input().split("|")
    piece, composer, key = line[0], line[1], line[2]
    collection_dict[piece] = [composer, key]

while True:
    line = input()
    if line == "Stop":
        break
    line = line.split("|")
    cmd = line
    if cmd[0] == "Add":
        piece, composer, key = cmd[1], cmd[2], cmd[3]
        collection_dict = add(collection_dict, piece, composer, key)
    elif cmd[0] == "Remove":
        piece = cmd[1]
        collection_dict = remove(collection_dict, piece)
    elif cmd[0] == "ChangeKey":
        piece, new_key = cmd[1], cmd[2]
        collection_dict = change_key(collection_dict, piece, new_key)

for k, v in collection_dict.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")

