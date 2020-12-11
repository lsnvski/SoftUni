def farm(materials, mats, junk):
    for i in range(0, len(materials), 2):
        key = materials[i + 1]
        value = int(materials[i])
        if key not in mats:
            if key not in junk:
                junk[key] = value
            else:
                junk[key] += value
        else:
            mats[key] += value
        if mats['shards'] >= 250 or mats['fragments'] >= 250 or mats['motes'] >= 250:
            break
    return mats, junk


dic1 = {'shards': 0, 'fragments': 0, 'motes': 0}
dic2 = {}
line = input().lower().split()
while line:
    dic1, dic2 = farm(line, dic1, dic2)
    if dic1['shards'] >= 250:
        print('Shadowmourne obtained!')
        dic1['shards'] -= 250
        break
    elif dic1['fragments'] >= 250:
        print('Valanyr obtained!')
        dic1['fragments'] -= 250
        break
    elif dic1['motes'] >= 250:
        print('Dragonwrath obtained!')
        dic1['motes'] -= 250
        break
    line = input().lower().split()
dic1 = dict(sorted(dic1.items(), key=lambda x: (-x[1], x[0])))
dic2 = dict(sorted(dic2.items(), key=lambda x: x[0]))
for key, value in dic1.items():
    print(f'{key}: {value}')
for key, value in dic2.items():
    print(f'{key}: {value}')