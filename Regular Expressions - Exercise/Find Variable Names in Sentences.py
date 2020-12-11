import re

string = input()

regex = r'(?<=\s_)[A-Za-z0-9]+(?![\d\S])'

variables = re.findall(regex, string)

print(",".join(variables))