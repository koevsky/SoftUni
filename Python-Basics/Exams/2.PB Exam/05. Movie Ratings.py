import sys
movie_count = int(input())

highest_value = -sys.maxsize
lowest_value = sys.maxsize
highest_name, lowest_name = "", ""
total = 0

for m in range(movie_count):
    movie_name = input()
    rating = float(input())
    if rating > highest_value:
        highest_value = rating
        highest_name = movie_name
    if rating < lowest_value:
        lowest_value = rating
        lowest_name = movie_name
    total += rating

print(f"{highest_name} is with highest rating: {highest_value:.1f}")
print(f"{lowest_name} is with lowest rating: {lowest_value:.1f}")
print(f"Average rating: {(total / movie_count):.1f}")