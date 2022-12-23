rooms = int(input())
chairs_left = 0
chairs_needed = False
for x in range(1, rooms+1):
    room_state = input().split(" ")
    chairs = room_state[0].count("X")
    people_in = int(room_state[-1])
    if chairs >= people_in:
        chairs_left += chairs - people_in
    else:
        chairs_needed = True
        print(f"{people_in - chairs} more chairs needed in room {x}")
if not chairs_needed:
    print(f"Game On, {chairs_left} free chairs left")