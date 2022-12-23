def tribonacci(n):

    res = [1]
    trib = [0, 0, 1]
    for x in range(n):
        res.append(sum(trib))
        trib.pop(0)
        trib.append(res[-1])
    return res


count = int(input()) - 1
result = [str(x) for x in tribonacci(count)]
print(" ".join(result))