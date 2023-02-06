from collections import deque

eggs_size = deque([int(x) for x in input().split(", ")])
pieces_paper = [int(x) for x in input().split(", ")]

box_counter = 0


while eggs_size and pieces_paper:

    egg_num = eggs_size[0]
    paper_wrap = pieces_paper[-1]

    if egg_num <= 0:
        eggs_size.popleft()
        continue

    elif egg_num == 13:
        eggs_size.popleft()
        pieces_paper[0], pieces_paper[-1] = pieces_paper[-1], pieces_paper[0]
        continue

    if egg_num + paper_wrap <= 50:
        box_counter += 1
        eggs_size.popleft()
        pieces_paper.pop()

    else:
        eggs_size.popleft()
        pieces_paper.pop()

if box_counter:
    print(f"Great! You filled {box_counter} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_size])}")

if pieces_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in pieces_paper])}")