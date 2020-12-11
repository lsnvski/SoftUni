import itertools

total_str = input().split(" ")

first_str = total_str[0]
second_str = total_str[1]

first_str = (x for x in first_str)
second_str = (x for x in second_str)

total_value = 0

for f, s in itertools.zip_longest(first_str, second_str, fillvalue=None):
    if f is None:
        total_value += ord(s)
    elif s is None:
        total_value += ord(f)
    else:
        total_value += int(ord(f)) * int(ord(s))

print(total_value)