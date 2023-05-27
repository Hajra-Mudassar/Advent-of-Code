with open ("day04.txt") as rucksacks:
    mainlist = [sack for sack in rucksacks.read().strip().split()]

print(mainlist)

totalnumber = 0
totalparttwo = 0

for each in mainlist:
    pairone, pairtwo = each.split(',')

    paironeset = [int(i) for i in pairone.split('-')]
    start = paironeset[0]
    stop = paironeset[1]
    lista = []
    for i in range(start, stop+1):
        lista.append(i)
    seta = set(lista)

    pairtwoset = [int(i) for i in pairtwo.split('-')]
    start = pairtwoset[0]
    stop = pairtwoset[1]
    listb = []
    for i in range(start, stop+1):
        listb.append(i)
    setb = set(listb)

    if seta.issubset(setb):
        totalnumber += 1
    elif setb.issubset(seta):
        totalnumber += 1

    if seta.intersection(setb):
        totalparttwo += 1


print(f"\nAnswer day04: {totalnumber}")
print(f"\nAnswer day04 part two: {totalparttwo}")
