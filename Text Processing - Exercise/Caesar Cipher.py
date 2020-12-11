
plain = input()

first_layer = (chr(ord(x) + 3) for x in plain)

for x in first_layer:
    print(x, end="")