def draw_figure(n):

    def top_part():
        res = []
        for x in range(n):
            empty_spaces = (n - x -1) * " "
            symbols = list((x + 1) * "*")
            res.append(empty_spaces + " ".join(symbols))

        return "\n".join(res)

    def bottom_part():
        res = []
        for x in range(n-1, 0, -1):
            empty_spaces = (n - x) * " "
            symbols = list(x * "*")
            res.append(empty_spaces + " ".join(symbols))

        return "\n".join(res)

    print(top_part())
    print(bottom_part())

draw_figure(int(input()))

