import re

pattern = r'(?P<sym>^@#{1,})[A-Z]{1}[a-zA-Z0-9]{4,}(?=[A-Z]@)[A-Z](?P=sym)$'

digi_patt = r'\d+'

lines = int(input())

for times in range(1, lines + 1):

    product = input()

    bar_code = re.match(pattern, product)

    if bar_code:

        check_group = re.findall(digi_patt, bar_code.string)
        if check_group:
            print("Product group: " + "".join(x for x in check_group))
        else:
            print("Product group: 00")
    else:
        print('Invalid barcode')


