rooms = int(input())
need = 0

for room in range(1, rooms + 1):
    chairs_complete = [int(x * 0) for x in range(1, rooms + 1)]

    chairs = input().split(" ")
    chairs_available = len(chairs[0])
    chairs_needed = int(chairs[1])

    if chairs_needed > chairs_available:
        needed = chairs_needed - chairs_available
        print(f'{needed} more chairs needed in room {room}')
        need -= needed

    elif chairs_available > chairs_needed:
        need += chairs_available - chairs_needed

if need >= 0:
    print(f'Game On, {need} free chairs left')

