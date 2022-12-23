last_sector = input()
first_sector_row_count = int(input())
places_per_odd_row = int(input())
place_counter = 0
for sectors in range(65, ord(last_sector)+1):
    for rows in range(1, first_sector_row_count+1):
        if rows % 2 != 0:
            for place in range(97, 97+places_per_odd_row):
                print(f"{chr(sectors)}{rows}{chr(place)}")
                place_counter += 1
        else:
            for place in range(97, 97+places_per_odd_row+2):
                print(f"{chr(sectors)}{rows}{chr(place)}")
                place_counter += 1
    first_sector_row_count += 1
print(place_counter)