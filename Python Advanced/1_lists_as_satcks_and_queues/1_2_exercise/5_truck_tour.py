from collections import deque

n = int(input())
gas_stations = deque([[int(x) for x in input().split()] for _ in range(n)])

fuel_left = 0
current_index = 0

while True:
    start_fuel, start_distance = gas_stations[0]
    if start_fuel >= start_distance:
        for station in gas_stations:
            station_fuel, station_distance = station
            current_fuel = station_fuel + fuel_left
            fuel_left = 0
            if current_fuel < station_distance:
                break
            else:
                fuel_left += current_fuel - station_distance - fuel_left
        else:
            break
    gas_stations.append(gas_stations.popleft())
    current_index += 1

print(current_index)
