space_bagaj = float(input())
bags = 0
volume = 0

while True:
    volume_bag = input()

    if volume_bag == "End":
        print(f"Congratulations! All suitcases are loaded!\n"
              f"Statistic: {bags} suitcases loaded.")
        break

    vb = float(volume_bag)
    temp_vol = volume + vb

    if temp_vol >= space_bagaj:
        print(f"No more space!\n"
              f"Statistic: {bags} suitcases loaded.")
        break

    bags += 1
    if bags % 3 == 0:
        volume += (vb + (vb * 0.1))
    else:
        volume += vb