from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar_stack = [int(x) for x in input().split()]
symbols = deque(input().split())

collected_nectar = []

while working_bees and nectar_stack:
    if working_bees[0] <= nectar_stack[-1]:
        operator = symbols.popleft()
        current_bee = working_bees.popleft()
        current_nectar = nectar_stack.pop()
        res = 0
        if operator == "+":
            res = abs(current_bee + current_nectar)
        elif operator == "-":
            res = abs(current_bee - current_nectar)
        elif operator == "*":
            res = abs(current_bee * current_nectar)
        elif operator == "/" and current_nectar != 0:
            res = abs(current_bee / current_nectar)
        collected_nectar.append(res)
    else:
        nectar_stack.pop()


print(f"Total honey made: {sum(collected_nectar)}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar_stack:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_stack])}")




