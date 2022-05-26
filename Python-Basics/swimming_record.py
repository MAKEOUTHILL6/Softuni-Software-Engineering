record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_distance = float(input())
needed_distance_to_swim = distance_in_meters * time_in_seconds_for_distance
additional_time = int(distance_in_meters / 15) * 12.5
total_time = additional_time + needed_distance_to_swim

if total_time < record_in_seconds:
    print(f'Yes! The new world record is {total_time:.2f} seconds !')
else:
    diff = total_time - record_in_seconds
    print(f'No! He was {diff:.2f} seconds slower!')
