guests_likes = {}
dislikes = 0

while True:

    lines = input()

    if lines == "Stop":
        break

    lines = lines.split("-")

    taste = lines[0]
    guest = lines[1]
    food = lines[2]

    if taste == "Like":

        if guest in guests_likes:

            if food in guests_likes[guest]:
                pass

            else:
                guests_likes[guest].append(food)
        else:
            guests_likes[guest] = [food]

    if taste == "Unlike":

        if guest not in guests_likes:
            print(f'{guest} is not at the party.')

        elif food not in guests_likes[guest]:
            print(f"{guest} doesn't have the {food} in his/her collection.")

        else:

            for meal in guests_likes[guest]:

                if food == meal:
                    guests_likes[guest].remove(food)
                    dislikes += 1
                    print(f"{guest} doesn't like the {food}.")

guests_likes = dict(sorted(guests_likes.items(), key=lambda x: x[0]))
guests_likes = dict(sorted(guests_likes.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in guests_likes.items():
    print(f'{key}: {", ".join(x for x in value)}')

print(f'Unliked meals: {dislikes}')
