from collections import deque
from datetime import datetime
robots_list = [x.split("-") for x in input().split(";")]
robots_dict = {x[0]: int(x[1]) for x in robots_list}
h, m, s = [int(x) for x in input().split(":")]
for x in range(len(robots_list)):
    robots_list[x][1] = int(robots_list[x][1])

products = deque([])
while True:
    line = input()
    if line == "End":
        break
    products.append(line)


def time_string(h, m, s):
    if s < 10:
        s = "0"+str(s)
    if m < 10:
        m = "0"+str(m)
    if h < 10:
        h = "0"+str(h)
    return f"{h}:{m}:{s}"


non_working_robots = deque(robots_list)
working_robots = deque([])
while products:
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0

    if working_robots:
        for x in range(len(working_robots)):
            working_robots[x][1] -= 1
            if working_robots[x][1] == 0:
                name = working_robots[x][0]
                non_working_robots.append([name, robots_dict[name]])
                working_robots[x] = ""
        while "" in working_robots:
            working_robots.remove("")

    if non_working_robots and products:
        name = non_working_robots[0][0]
        product = products.popleft()
        print(f"{name} - {product} [{time_string(h, m, s)}]")
        working_robots.append(non_working_robots.popleft())
    else:
        products.append(products.popleft())


