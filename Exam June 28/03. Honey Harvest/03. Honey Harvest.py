flower_type = input()
count_flowers = int(input())
season = input()

total_produced = 0


if season == "Spring":
    total_season = 0
    if flower_type == "Sunflower":
        total_season = count_flowers * 10
    if flower_type == "Daisy":
        total_season = (count_flowers * 12) + ((count_flowers * 12) * 0.1)
    if flower_type == "Lavender":
        total_season = count_flowers * 12
    if flower_type == "Mint":
        total_season = (count_flowers * 10) + ((count_flowers * 10) * 0.1)
    total_produced = total_season

if season == "Summer":
    total_season = 0
    if flower_type == "Sunflower":
        total_season = count_flowers * 8
    if flower_type == "Daisy":
        total_season = count_flowers * 8
    if flower_type == "Lavender":
        total_season = count_flowers * 8
    if flower_type == "Mint":
        total_season = count_flowers * 12
    total_produced = total_season + (total_season * 0.1)

if season == "Autumn":
    total_season = 0
    if flower_type == "Sunflower":
        total_season = count_flowers * 12
    if flower_type == "Daisy":
        total_season = count_flowers * 6
    if flower_type == "Lavender":
        total_season = count_flowers * 6
    if flower_type == "Mint":
        total_season = count_flowers * 6
    total_produced = total_season - (total_season * 0.05)

print(f"Total honey harvested: {total_produced:.2f}")