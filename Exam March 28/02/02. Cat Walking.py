lenght_min = int(input())
times_per_day = int(input())
calories = int(input())

calories_burned = lenght_min * times_per_day * 5

if calories_burned >= calories * 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")