length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
total_volume = volume - (volume*percent/100)
print(total_volume/1000)
