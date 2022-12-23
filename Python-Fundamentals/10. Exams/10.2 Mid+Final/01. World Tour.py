def add_stop(string, idx, new_string):
    if 0 <= idx <= len(string)-1:
        string = string[:idx] + new_string + string[idx:]
    print(string)
    return string


def remove_stop(string, s_idx, e_idx):
    condition1 = s_idx <= e_idx
    condition2 = 0 <= s_idx <= len(string) - 1
    condition3 = 0 <= e_idx <= len(string) - 1
    if condition1 and condition2 and condition3:
        string = string[:s_idx] + string[e_idx+1:]
    print(string)
    return string


def switch(string, old_string, new_string):
    string = str(string)
    if old_string in string:
        string = string.replace(old_string, new_string)
    print(string)
    return string


destinations_string = input()
while True:
    line = input()
    if line == "Travel":
        break
    cmd = line.split(":")
    if cmd[0] == "Add Stop":
        index, new_stop = int(cmd[1]), cmd[2]
        destinations_string = add_stop(destinations_string, index, new_stop)
    elif cmd[0] == "Remove Stop":
        start_ind, end_index = int(cmd[1]), int(cmd[2])
        destinations_string = remove_stop(destinations_string, start_ind, end_index)
    elif cmd[0] == "Switch":
        old_str, new_str = cmd[1], cmd[2]
        destinations_string = switch(destinations_string, old_str, new_str)

print(f"Ready for world tour! Planned stops: {destinations_string}")