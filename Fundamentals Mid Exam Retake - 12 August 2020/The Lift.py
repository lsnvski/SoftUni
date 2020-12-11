people_queue = int(input())
lift_state = str(input()).split(" ")
lift_state = [int(i) for i in lift_state]

while people_queue > 0:

    if sum(lift_state) == 4 * len(lift_state):
        break

    for index, number in enumerate(lift_state):
        people_cabin = 4 - number

        if people_cabin >= people_queue:
            lift_state[index] = people_queue
            people_queue = 0
            break

        else:
            lift_state[index] = 4
            people_queue -= people_cabin

people_needed = sum([4 - x for x in lift_state])

if people_needed > people_queue:
    print("The lift has empty spots!")
    for x in lift_state:
        print(x, end=" ")

elif people_needed < people_queue:
    print(f"There isn't enough space! {people_queue} people in a queue!")
    for x in lift_state:
        print(x, end=" ")