def trapped_check(str_list, rows):
    row_count = int(rows)
    column_count = None
    str_list = list(str_list)
    labyrinth_list = str_list

    kate_row, kate_column = None, None
    top_wall, bottom_wall = None, None
    left_wall, right_wall = None, None

    is_trapped = False
    #   finds if kate is trapped between top or bottom wall #
    for x in range(len(labyrinth_list)):
        row = labyrinth_list[x]
        column_count = len(row)
        if "k" in row:
            kate_row = int(x)
            kate_column = row.index("k")
        if row == column_count * "#" and not kate_row and not kate_column:
            top_wall = x
        if row == column_count * "#" and kate_row and kate_column:
            bottom_wall = x
    #   finds if kate is trapped between top or bottom wall #
    if 0 < kate_column < column_count:
        for lc in range(0, kate_column):
            l_wall = ""
            for r in range(row_count):
                if labyrinth_list[r][lc] == "#":
                    l_wall += "#"
            if l_wall == row_count * "#":
                left_wall = lc

        for rc in range(kate_column, column_count):
            r_wall = ""
            for r in range(row_count):
                if labyrinth_list[r][rc] == "#":
                    r_wall += "#"
            if r_wall == row_count * "#":
                right_wall = rc

    if str(left_wall).isdigit() and str(right_wall).isdigit() and str(top_wall).isdigit() and str(
            bottom_wall).isdigit():
        if (left_wall < kate_column < right_wall) and (top_wall < kate_row < bottom_wall):
            is_trapped = True
    else:
        is_trapped = False
    return is_trapped


def find_way_out(str_list, rows):
    labyrinth = [list(x) for x in str_list] # convert every string to a list

    row_count, column_count = rows, len(labyrinth[0]) # labyrinth dimensions
    kate_row, kate_column = None, None # kate position in labyrinth
    exit_points = [] # list of possible exit points
    #   Finds kate position   #
    for e in range(len(labyrinth)):
        if "k" in labyrinth[e]:
            kate_row = e
            kate_column = labyrinth[e].index("k")
    #   Finds possible exits  #
    for r in range(len(labyrinth)):     # for every row
        for c in range(len(labyrinth[r])): # for every column
            if (r == 0 or r == row_count - 1) and labyrinth[r][c] == " ": # check if there are exits on TOP or BOTTOM wall
                exit_coordinates = [r, c]
                exit_points.append(exit_coordinates) # save the coordinates to a list
            if (0 < r < row_count - 1) and (labyrinth[r][0] == " " or labyrinth[r][-1] == " "): # check if there are exits on LEFT or RIGHT wall
                exit_coordinates = [r, c]
                exit_points.append(exit_coordinates) # save the coordinates to a list
    #   for every possible exit, find count of turns  #
    for p in range(len(exit_points)):
        moves_count = 0
        moves_list = []
        kate_last_r, kate_last_c = kate_row, kate_column

        for r in range(row_count):
            for c in range(column_count):





rows_count = int(input())
maze = [input() for x in range(rows_count)]
if trapped_check(maze, rows_count):
    print("Kate cannot get out")
else:
    print(find_way_out(maze, rows_count))


