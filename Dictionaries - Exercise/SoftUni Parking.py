def db_check_register(user, licence):
    if user in database.keys():
        print(f"ERROR: already registered with plate number {licence}")
    else:
        database[user] = licence
        print(f"{user} registered {licence} successfully")


def db_check_unregister(user):
    if user in database.keys():
        del database[user]
        print(f"{user} unregistered successfully")
    else:
        print(f"ERROR: user {user} not found")


lines = int(input())

database = {}

for car in range(1, lines + 1):
    user_car = input().split()

    action = user_car[0]
    username = user_car[1]

    if len(user_car) == 3 and action == "register":
        plate = user_car[2]
        db_check_register(username, plate)

    elif len(user_car) < 3 and action == "unregister":
        db_check_unregister(username)

for key, value in database.items():
    print(f"{key} => {value}")

