width = int(input())
length = int(input())
cake_size = width * length
while True:
    data = input()
    if data == "STOP":
        print(f"{cake_size} pieces are left.")
        break
    piece_count = int(data)
    if cake_size - piece_count < 0:
        pieces_needed = abs(cake_size - piece_count)
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        break

    cake_size -= piece_count