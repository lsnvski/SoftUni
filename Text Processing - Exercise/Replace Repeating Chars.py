from itertools import groupby

string = input()

print("".join(s for s, _ in groupby(string)))
