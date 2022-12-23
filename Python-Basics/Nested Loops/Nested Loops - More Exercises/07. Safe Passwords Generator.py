#########
a = int(input())
b = int(input())
max_count_pas = int(input())
counter, sym_A, sym_B = 0, 35, 64
is_break = False
for x in range(1, a+1):
    if is_break:
        break
    for y in range(1, b + 1):
        password = chr(sym_A) + chr(sym_B) + str(x) + str(y) + chr(sym_B) + chr(sym_A)
        print(password, end="|")
        sym_A += 1
        sym_B += 1
        counter += 1
        if sym_A > 55:
            sym_A = 35
        if sym_B > 96:
            sym_B = 64
        if counter == max_count_pas:
            is_break = True
            break



