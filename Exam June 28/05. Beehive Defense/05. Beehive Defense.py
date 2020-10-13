bees = int(input())
hp = int(input())
atk = int(input())

while True:
    if bees < 100:
        break
    if hp <= 0:
        break
    bees = (bees - atk)
    hp -= (bees * 5)

if bees < 0:
    bees = 0
if bees > 100:
    print(f"Beehive won! Bees left {bees}.")
else:
    print(f"The bear stole the honey! Bees left {bees}.")