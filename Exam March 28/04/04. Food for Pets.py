days = int(input())
food = int(input())

total_dog = 0
total_cat = 0
bisc = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    total_dog += dog_food
    total_cat += cat_food

    if day % 3 == 0:
        bisc += (dog_food + cat_food) * 0.1

eaten = total_dog + total_cat
total_eaten = (eaten / food) * 100
dog = (total_dog / eaten) * 100
cat = (total_cat / eaten) * 100

print(f"Total eaten biscuits: {round(bisc)}gr.\n"
      f"{total_eaten:.2f}% of the food has been eaten.\n"
      f"{dog:.2f}% eaten from the dog.\n"
      f"{cat:.2f}% eaten from the cat.\n")