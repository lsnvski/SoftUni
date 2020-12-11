bees = int(input()) * 0.21
flowers = int(input())

total = bees * flowers
fill = total // 100
left = total % 100

print(f'{fill:.0f} honeycombs filled.\n'
      f'{left:.2f} grams of honey left.')
