n = int(input())
matrix = [list(input()) for _ in range(n)]
searched_symbol = input()
for row in range(n):
    if searched_symbol in matrix[row]:
        searched_symbol_position = (row, matrix[row].index(searched_symbol))
        print(searched_symbol_position)
        break
else:
    print(f"{searched_symbol} does not occur in the matrix")