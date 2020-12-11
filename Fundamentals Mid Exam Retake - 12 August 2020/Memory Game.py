def check_input(index1, index2, move, len):
    if 0 <= index1 <= len and 0 <= index2 <= len:
        return True

    else:
        elements_list.insert(move * 2, f'-{move}a')
        elements_list.insert((move * 2) + 1, f'-{move}a')
        return False


def match(index1, index2):
    element1 = elements_list[index1]
    element2 = elements_list[index2]

    if element1 == element2:
        elements_list.remove(element1)
        elements_list.remove(element2)
        return [True, element1]

    else:
        return False


elements_list = str(input()).split(" ")
elements_list = [x for x in elements_list if x != ""]
moves = 0

while True:
    len_elements = len(elements_list) - 1
    command = str(input())

    if not bool(elements_list) or command == "end":
        break

    command = command.split(" ")
    command = [x for x in command if x != ""]
    moves += 1
    command = [int(x) for x in command]

    if check_input(command[0], command[1], moves, len_elements):
        check_match = match(command[0], command[1])
        if not check_match:
            print("Try again!")
        else:
            print(f"Congrats! You have found matching elements - {check_match[1]}!")
    else:
        print("Invalid input! Adding additional elements to the board")


if bool(elements_list):
    print("Sorry you lose :(")
    print(" ".join(elements_list))
else:
    print(f"You have won in {moves} turns!")
