import re
n = int(input())
star_pattern = r"([star])"
search_pattern = r"@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([A|D])![^@\-!:>]*\->(\d+)"

attacked_planets = []
destroyed_planets = []

for _ in range(n):
    line = input()
    star_count = len(re.findall(star_pattern, line, re.IGNORECASE))
    decrypted_message = "".join([chr(ord(x)-star_count) for x in line])

    searched = re.findall(search_pattern, decrypted_message)
    if searched:
        planet = searched[0][0]
        population = searched[0][1]
        attack_type = searched[0][2]
        soldier_count = searched[0][3]
        if attack_type == "D":
            destroyed_planets.append(planet)
        elif attack_type == "A":
            attacked_planets.append(planet)

attacked_planets.sort()
destroyed_planets.sort()
print(f"Attacked planets: {len(attacked_planets)}")
for p in attacked_planets:
    print(f"-> {p}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for p in destroyed_planets:
    print(f"-> {p}")
