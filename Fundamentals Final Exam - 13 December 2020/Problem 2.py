import re


def enc(tup):
    yield "".join(x for x in tup)


lines = int(input())

regex = r'(?P<sym>^\w+|^\W+)>(?P<nums>\d{3})\|(?P<lc>[a-z]{3})\|(?P<uc>[A-Z]{3})\|(?P<sym1>[^<>]{3})<(?P=sym)'

for times in range(1, lines + 1):
    raw_password = input()

    new = re.match(regex, raw_password)

    if not new:
        print("Try another password!")
    else:
        encrypted = new.group('nums', 'lc', 'uc', 'sym1')

        for x in enc(encrypted):
            print(f"Password: {x}")
