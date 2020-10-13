amount_food_kg = int(input()) * 1000
total_eaten = 0

while True:
    food_day_g = input()
    if food_day_g == "Adopted":
        break


    total_eaten += int(food_day_g)


if amount_food_kg >= total_eaten:
    print(f"Food is enough! Leftovers: {amount_food_kg - total_eaten} grams.")
else:
    print(f"Food is not enough. You need {total_eaten - amount_food_kg} grams more.")