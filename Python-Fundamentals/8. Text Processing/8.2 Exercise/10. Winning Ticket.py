tickets = map(str.strip, input().split(","))
for ticket in tickets:
    if len(ticket) == 20:
        is_winner = False
        first_half = ticket[:int(len(ticket)/2)]
        second_half = ticket[int(len(ticket)/2):]
        symbol_list = ["@", "#", "$", "^"]
        symbol = ""
        for x in symbol_list:
            if is_winner:
                break
            if first_half.count(x) >= 6 and second_half.count(x) >= 6:
                variants = list(reversed([x*y for y in range(6, 11)]))
                res = [var for var in variants if var in first_half and var in second_half]
                if res:
                    symbol = res[0]
                    is_winner = True
                    break
        if is_winner:
            if 6 <= len(symbol) < 10:
                print(f'ticket "{ticket}" - {len(symbol)}{symbol[0]}')
            elif len(symbol) == 10:
                print(f'ticket "{ticket}" - {len(symbol)}{symbol[0]} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")