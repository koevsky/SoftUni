def loading_bar(num):
    if num < 100:
        return f"{num}% [{'%'*(num//10)+(10-(num//10))*'.'}]\nStill loading..."
    return f"{num}% Complete!\n[{(num//10)*'%'}]"

x = int(input())
print(loading_bar(x))
