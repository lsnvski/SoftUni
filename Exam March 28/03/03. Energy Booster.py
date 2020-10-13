W_small = 56 * 2
W_big = 28.70 * 5

M_small = 36.66 * 2
M_big = 19.60 * 5

P_small = 42.10 * 2
P_big = 24.80 * 5

R_small = 20 * 2
R_big = 15.20 * 5

fruit = input()
type_fruit = input()
count = int(input())

total = 0

if fruit == "Watermelon":
    if type_fruit == "small":
        total = W_small * count
    if type_fruit == "big":
        total = W_big * count

if fruit == "Mango":
    if type_fruit == "small":
        total = M_small * count
    if type_fruit == "big":
        total = M_big * count

if fruit == "Pineapple":
    if type_fruit == "small":
        total = P_small * count
    if type_fruit == "big":
        total = P_big * count

if fruit == "Raspberry":
    if type_fruit == "small":
        total = R_small * count
    if type_fruit == "big":
        total = R_big * count

if 400 <= total <= 1000:
    total = total - (total * 0.15)
elif total > 1000:
    total = total - (total * 0.5)

print(f"{total:.2f} lv.")