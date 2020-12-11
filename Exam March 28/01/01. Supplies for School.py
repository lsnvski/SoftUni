himihalhi = int(input()) * 5.80
marker = int(input()) * 7.20
preparat = float(input()) * 1.20

total = himihalhi + marker + preparat
total_of_total = total - (total * (int(input()) / 100))
print(f"{total_of_total:.3f}")