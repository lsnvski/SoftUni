numbers = input().split(" ")
numbers = sorted(numbers, reverse=True)

for num in numbers:
    print(num, end="")