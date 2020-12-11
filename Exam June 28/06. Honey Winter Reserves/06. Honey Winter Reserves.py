honey_needed = float(input())
honey_collected = 0

while True:
    name = input()
    if name == "Winter has come":
        break
    total_hon_collected = 0

    for month in range(1, 7):
        total_hon_collected += float(input())

    if total_hon_collected < 0:
        print(f"{name} was banished for gluttony")

    honey_collected += total_hon_collected
    if honey_collected >= honey_needed:
        break


if honey_needed > honey_collected:
    print(f"Hard Winter! Honey needed {honey_needed - honey_collected:.2f}.")
elif honey_collected >= honey_needed:
    print(f"Well done! Honey surplus {honey_collected - honey_needed:.2f}.")