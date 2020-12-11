employee1 = int(input())
employee2 = int(input())
employee3 = int(input())

total_per_hour = employee1 + employee2 + employee3

people = int(input())
hours = 0
pochivki_count = 0

while people > 0:
    hours += 1
    people = people - total_per_hour

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
