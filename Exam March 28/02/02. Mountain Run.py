import math

record = float(input())
meter_per_sec = float(input())
time_for_meter = float(input())

time = (math.floor(meter_per_sec / 50) * 30) + (meter_per_sec * time_for_meter)

if record > time:
    print(f"Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {time - record:.2f} seconds slower.")