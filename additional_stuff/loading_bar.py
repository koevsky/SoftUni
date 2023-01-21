import os
from tqdm import tqdm
from colorama import Fore
import time

for i in tqdm(range(100),
    desc= Fore.GREEN + "Loading. . .",
    ascii=False, ncols=75):
    time.sleep(0.01)

print(Fore.GREEN + "Complete. . .")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')