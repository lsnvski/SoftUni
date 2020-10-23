version = input().split(".")
version = [int(x) for x in version]
new_version = [(lambda x: True if x + 1 == 10 else False)(x) for x in version]


def add_version(iterable1, iterable2):
    new_list_version = iterable2

    if not any(iterable1):
        new_list_version[-1] = new_list_version[-1] + 1
        return new_list_version

    if iterable1[1] and not iterable1[-1]:
        new_list_version[-1] = iterable2[-1] + 1
    elif not iterable1[1] and iterable1[-1]:
        new_list_version[-1], new_list_version[1] = 0, new_list_version[1] + 1
    elif iterable1[-1] and iterable1[1]:
        new_list_version[0], new_list_version[1], new_list_version[-1] = new_list_version[0] + 1, 0, 0

    return new_list_version


version = add_version(new_version, version)
version.insert(1, ".")
version.insert(3, ".")
for i in version:
    print(i, end="")
