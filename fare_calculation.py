def calculate_fare(distance_km):
    base_fare = 50
    rate_per_km = 10
    return base_fare + (distance_km * rate_per_km)

trips = [5, 10, 3]  

total_fare = 0

for index, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {index}: ${fare}")

print(f"Total Fare: ${total_fare}")
