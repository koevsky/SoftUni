import math
centuries = int(input())
years = centuries * 100
days = math.floor(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {int(days)} days = {int(hours)} hours = {int(minutes)} minutes")