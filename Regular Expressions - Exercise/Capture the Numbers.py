import re

to_parse = ""

while True:
    string = input()

    if string == "":
        break

    to_parse += string


print(" ".join(re.findall(r'\d+', to_parse)))