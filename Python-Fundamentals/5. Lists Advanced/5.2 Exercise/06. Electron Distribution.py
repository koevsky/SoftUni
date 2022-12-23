def el_distribute(num):
    shell = []
    x = 1
    while num - 2 * x ** 2 > 0:
        num -= 2 * x ** 2
        shell.append(2 * x ** 2)
        x += 1
    shell.append(num)
    return shell


numb = int(input())
print(el_distribute(numb))
