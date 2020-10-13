population = int(input())
years = int(input())


for year in range(1,years + 1):
    new = int(population / 10) * 2
    population = population + new
    if year % 5 == 0:
        migrant = int(population / 50) * 5
        population = population - migrant
    dead = int(population / 20) * 2
    population = (population - dead)

print(f"Beehive population: {population}")
