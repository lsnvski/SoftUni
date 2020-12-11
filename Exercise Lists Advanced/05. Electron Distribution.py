<<<<<<< HEAD
electrons = int(input())

electrons_shell = [2 * (x ** 2) for x in range(1, electrons + 1) if 2 * (x ** 2) < electrons]
shells_filled = []

for fill in electrons_shell:
    if electrons > fill:
        electrons -= fill
        shells_filled.append(fill)

    if fill > electrons > 0:
        shells_filled.append(electrons)
        electrons -= fill

print(shells_filled)

=======
electrons = int(input())

electrons_shell = [2 * (x ** 2) for x in range(1, electrons + 1) if 2 * (x ** 2) < electrons]
shells_filled = []

for fill in electrons_shell:
    if electrons > fill:
        electrons -= fill
        shells_filled.append(fill)

    if fill > electrons > 0:
        shells_filled.append(electrons)
        electrons -= fill

print(shells_filled)

>>>>>>> 208b47ea4d0bcafc85cf570be2bfb1f6ac828c17
