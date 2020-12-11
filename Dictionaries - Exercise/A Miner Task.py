mined = {}

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())
    key = mined.keys()

    if resource not in key:
        mined[resource] = quantity
    else:
        mined[resource] += quantity

for key in mined.keys():
    print(f'{key} -> {mined[key]}')