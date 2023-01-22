from collections import deque

def fill_the_box(h, l, w, *args):

    box_volume = h * l * w
    args = deque(args)

    while args:

        x = args[0]

        if x == "Finish":
            break

        num = int(x)

        if num < box_volume:
            box_volume -= num
            args.popleft()
        else:
            num -= box_volume
            box_volume = 0
            args[0] = num
            break

    if box_volume > 0:
        return f"There is free space in the box. You could put {box_volume} more cubes."
    else:
        args.remove("Finish")
        return f"No more free space! You have {sum(args)} more cubes."



print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))




