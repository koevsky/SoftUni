payload_count = int(input())

bus_payload = 0
truck_payload = 0
train_payload =  0

for x in range(payload_count):
    payload_weight = int(input())

    if payload_weight <= 3:
        bus_payload += payload_weight
    elif 4 <= payload_weight <= 11:
        truck_payload += payload_weight
    elif payload_weight >= 12:
        train_payload += payload_weight

total_weight = bus_payload + truck_payload + train_payload
average_price = (bus_payload * 200 + truck_payload * 175 + train_payload * 120) / total_weight


bus_percentage = bus_payload / total_weight * 100
truck_percentage = truck_payload / total_weight * 100
train_percentage = train_payload / total_weight * 100

print(f"{average_price:.2f}")
print(f"{bus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")