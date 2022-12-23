def add(seq, count):
    seq[-1] += count
    return seq


def insert(seq, index, count):
    seq[index] += count
    return seq


def leave(seq, index, count):
    seq[index] -= count
    return seq


wagons_count = int(input())
wagons_list = [0 for x in range(wagons_count)]
while True:
    text = input()
    if text == "End":
        print(wagons_list)
        break
    text = text.split(" ")
    if "add" in text:
        people = int(text[1])
        wagons_list = add(wagons_list, people)
    elif "insert" in text:
        position = int(text[1])
        people = int(text[2])
        wagons_list = insert(wagons_list, position, people)
    elif "leave" in text:
        position = int(text[1])
        people = int(text[2])
        wagons_list = leave(wagons_list,position, people)