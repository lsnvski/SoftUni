neighborhood = input().split("@")
neighborhood = [int(x) for x in neighborhood]

houses_index = 0


def check(number):
    if number <= 0:
        return True
    elif number == 2 or number - 2 < 0:
        return None
    elif number - 2 > 0:
        return "False"


while True:
    command = input()
    if command == "Love!":
        break

    command = command.replace("{", "").replace("}", "")
    command = int(command.split(" ")[1])
    houses_index += command

    if houses_index > len(neighborhood) - 1:
        houses_index = 0

        if check(neighborhood[0]) is "False":
            neighborhood[0] = neighborhood[0] - 2

        elif check(neighborhood[0]):
            neighborhood[0] = 0
            print(f"Place {0} already had Valentine's day.")

        elif check(neighborhood[0]) is None:
            print(f"Place {0} has Valentine's day.")
            neighborhood[0] = neighborhood[0] - 2

    elif houses_index in range(len(neighborhood)):

        if check(neighborhood[houses_index]) is "False":
            neighborhood[houses_index] = neighborhood[houses_index] - 2

        elif check(neighborhood[houses_index]):
            neighborhood[houses_index] = 0
            print(f"Place {houses_index} already had Valentine's day.")

        elif check(neighborhood[houses_index]) is None:
            print(f"Place {houses_index} has Valentine's day.")
            neighborhood[houses_index] = neighborhood[houses_index] - 2

print(f"Cupid's last position was {houses_index}.")
fails = [x != 0 for x in neighborhood].count(True)
if sum(neighborhood) == 0:
    print("Mission was succesful.")
else:
    print(f"Cupid has failed {fails} places.")