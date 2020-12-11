gym_m = 42
gym_f = 35
box_m = 41
box_f = 37
yoga_m = 45
yoga_f = 42
zumba_m = 34
zumba_f = 31
dances_m = 51
dances_f = 53
pilates_m = 39
pilates_f = 37

money = float(input())
sex = input()
age = int(input())
sport = input()

total = 0

if sport == "Gym":
    if sex == "m":
        total = gym_m
    if sex == "f":
        total = gym_f

if sport == "Boxing":
    if sex == "m":
        total = box_m
    if sex == "f":
        total = box_f

if sport == "Yoga":
    if sex == "m":
        total = yoga_m
    if sex == "f":
        total = yoga_f

if sport == "Zumba":
    if sex == "m":
        total = zumba_m
    if sex == "f":
        total = zumba_f

if sport == "Dances":
    if sex == "m":
        total = dances_m
    if sex == "f":
        total = dances_f

if sport == "Pilates":
    if sex == "m":
        total = pilates_m
    if sex == "f":
        total = pilates_f

if age <= 19:
    total = total - (total * 0.2)

if money >= total:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${total - money:.2f} more.")