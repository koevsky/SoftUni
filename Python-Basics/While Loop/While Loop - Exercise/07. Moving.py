width, length, height, = int(input()), int(input()), int(input())
free_volume = width * length * height

while True:
    data = input()
    if data == "Done":
        space_left = free_volume
        print(f"{space_left} Cubic meters left.")
        break
    box_volume = int(data)
    if free_volume - box_volume <= 0:
        space_needed = box_volume - free_volume
        print(f"No more free space! You need {space_needed} Cubic meters more.")
        break
    free_volume -= box_volume