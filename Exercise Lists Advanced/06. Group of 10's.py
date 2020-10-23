numbers = input().split(", ")
numbers = [int(x) for x in numbers]

groups = {key: 0 for key in [x for x in range(10, max(numbers) + 10, 10)]}


def where(iter_key, iter_value):
    for key in iter_key:
        to_append = []
        for value in iter_value:
            if value <= key:
                to_append.append(value)

        iter_key[key] = to_append
        iter_value = [x for x in iter_value if x not in to_append]

    return iter_key


final = where(groups, numbers)
for i in final:
    print(f"Group of {i}'s: {final[i]}")



