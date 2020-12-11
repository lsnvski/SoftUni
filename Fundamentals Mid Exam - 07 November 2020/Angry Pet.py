itmes = input().split(" ")
items = [int(x) for x in itmes]

entry = int(input())
type_expense = input()
price_rate = input()

entry_item = items[entry]
left = items[0:entry]
right = items[entry + 1:]
total_left = 0
total_right = 0

if price_rate == "positive":
    left, right = [x for x in left if x > 0], [x for x in right if x > 0]
elif price_rate == "negative":
    left, right = [x for x in left if x < 0], [x for x in right if x < 0]

if type_expense == "cheap":
    total_left = sum([x for x in left if x < entry_item])
    total_right = sum([x for x in right if x < entry_item])

elif type_expense == "expensive":
    total_left = sum([x for x in left if x >= entry_item])
    total_right = sum([x for x in right if x >= entry_item])

elif type_expense == "all":
    total_left = sum(left)
    total_right = sum(right)

if total_left > total_right:
    print(f'Left - {total_left}')
elif total_left < total_right:
    print(f'Right - {total_right}')
elif total_left == total_right:
    print(f'Left - {total_left}')