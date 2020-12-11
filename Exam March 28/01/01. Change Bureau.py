btc = 1168
jpn = 0.15
usd = 1.76
eur = 1.95

in_euro = float(int(input()) * btc) + (float(input()) * (jpn * usd))
in_euro1 = in_euro / eur

swap = in_euro1 - (in_euro1 * (float(input()) / 100))

print(f"{swap:.2f}")
