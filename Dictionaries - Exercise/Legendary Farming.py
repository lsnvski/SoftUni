def check_legendary(items1, numbers):
    if items1 == "shards":
        legendary_items["Shadowmourne"] += numbers
    elif items1 == "fragments":
        legendary_items["Valanyr"] += numbers
    elif items1 == "motes":
        legendary_items["Dragonwrath"] += numbers


def sort_dict(dictionary, isalpha=False, reverse=False):
    if isalpha:
        return dict(sorted(dictionary.items(), key=lambda x: x[0]))
    else:
        if reverse:
            return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        if not reverse:
            return dict(sorted(dictionary.items(), key=lambda x: x[1]))

legendary_items = {
    "Shadowmourne": 0,
    "Valanyr": 0,
    "Dragonwrath": 0,
}

junk_items = {}

valid_legendary = [
    "shards",
    "fragments",
    "motes",
]

while True:
    switch = False

    for key, leg_item in legendary_items.items():
        if leg_item >= 250:
            legendary_items[key] -= 250
            switch = True
            print(f'{key} obtained!')
    if switch:
        break

    items = input().split(" ")
    dict_items = dict(zip(items[1::2], items[::2]))

    for item in dict_items.keys():
        check_item = item.lower()
        if check_item in valid_legendary:
            check_legendary(check_item, int(dict_items[item]))
        elif check_item in junk_items.keys():
            junk_items[item] += int(dict_items[item])
        else:
            junk_items[item] = int(dict_items[item])

legendary_items = dict(zip(valid_legendary, legendary_items.values()))
legendary_items = sort_dict(legendary_items, reverse=True)
junk_items = sort_dict(junk_items, isalpha=True)

for key, element in legendary_items.items():
    print(f'{key.lower()}: {element}')
for key, element in junk_items.items():
    print(f'{key}: {element}')