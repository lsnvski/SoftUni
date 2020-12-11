import re

string = input()
word = input()

pattern = f'\\b{word}\\b'

final = re.findall(pattern, string, re.IGNORECASE)

print(len(final))