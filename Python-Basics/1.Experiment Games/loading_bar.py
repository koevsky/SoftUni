from time import sleep
print("LOADING: ", end="")
for x in range(1, 20+1):
    sleep(0.3)
    print("#", end="")
print(f" {(x/20*100):.2f}%", end="")