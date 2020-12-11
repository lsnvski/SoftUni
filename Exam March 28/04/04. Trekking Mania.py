group = int(input())
total_people = 0

musala = 0
monblan = 0
kili = 0
K2 = 0
everest = 0

for i in range(1, group + 1):
    people = int(input())
    total_people += people

    if people <= 5:
        musala += people
    if 5 < people <= 12:
        monblan += people
    if 12 < people <= 25:
        kili += people
    if 25 < people <= 40:
        K2 += people
    if 40 < people:
        everest += people

print(f"{(musala / total_people) * 100:.2f}%\n"
      f"{(monblan / total_people) * 100:.2f}%\n"
      f"{(kili / total_people) * 100:.2f}%\n"
      f"{(K2 / total_people) * 100:.2f}%\n"
      f"{(everest / total_people) * 100:.2f}%\n")
