import re

data = input()

template = r'(?P<user>(?<=\s)[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@)(?P<host>[a-zA-Z]+(\-[a-z]+|\.[a-z]+)+)'

matches = re.finditer(template, data)

print("\n".join(x.group() for x in matches))

