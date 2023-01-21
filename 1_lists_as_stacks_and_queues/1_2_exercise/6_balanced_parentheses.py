parentheses = list(input())
index_stack = []

for i in range(len(parentheses)):
    char = parentheses[i]
    if char in ["(", "[", "{"]:
        index_stack.append(i)
    else:

        if not index_stack:
            print("NO")
            break
        last_index = index_stack[-1]

        if char == ")" and parentheses[last_index] == "(":
            index_stack.pop()
        elif char == "]" and parentheses[last_index] == "[":
            index_stack.pop()
        elif char == "}" and parentheses[last_index] == "{":
            index_stack.pop()
        else:
            print("NO")
            break
else:
    if not index_stack:
        print("YES")
    else:
        print("NO")
