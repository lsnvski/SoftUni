initial_list = input().split("!")


def urgent(item):
    if item not in initial_list:
        initial_list.insert(0, item)


def unnecessary(item):
    if item in initial_list:
        initial_list.remove(item)


def correct(old_item, item):
    if old_item in initial_list:
        ind = initial_list.index(old_item)
        initial_list[ind] = item


def rearrange(item):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)


while True:
    commands = input()

    if commands == "Go Shopping!":
        break

    commands = commands.split(" ")

    if len(commands) == 2:
        to_do = commands[0]
        grocery = commands[1]

    elif len(commands) == 3:
        to_do = commands[0]
        grocery_old = commands[1]
        grocery_new = commands[2]

    if to_do == "Urgent":
        urgent(grocery)

    elif to_do == "Unnecessary":
        unnecessary(grocery)

    elif to_do == "Correct":
        correct(grocery_old, grocery_new)

    elif to_do == "Rearrange":
        rearrange(grocery)

print(str(initial_list).replace("[", "").replace("]","").replace("'",""))



