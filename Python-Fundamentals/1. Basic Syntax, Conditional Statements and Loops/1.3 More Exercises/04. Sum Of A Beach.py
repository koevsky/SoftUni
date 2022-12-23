text = input().lower()
water_count = text.count("water")
fish_count = text.count("fish")
sand_count = text.count("sand")
sun_count = text.count("sun")
total = water_count + fish_count + sun_count + sand_count
print(total)