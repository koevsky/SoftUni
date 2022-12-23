def move(lst, num):
    lst = lst[num:] + lst[:num]
    return lst


def insert(idx, val, lst):
    lst = lst[:idx] + val + lst[idx:]
    return lst


def change_all(lst, subs, repl):
    new_lst = lst.replace(subs, repl)
    return new_lst


encrypted_message = input()
while True:
    line = input()
    if line == "Decode":
        print(f'The decrypted message is: {encrypted_message}')
        break
    cmd = line.split("|")
    if cmd[0] == "Move":
        num = int(cmd[1])
        encrypted_message = move(encrypted_message, num)
    elif cmd[0] == "Insert":
        index, value = int(cmd[1]), cmd[2]
        encrypted_message = insert(index, value, encrypted_message)
    elif cmd[0] == "ChangeAll":
        subst, replacement = cmd[1], cmd[2]
        encrypted_message = change_all(encrypted_message, subst, replacement)
