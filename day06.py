with open ("day06.txt") as buffer:
    str = buffer.read().strip()

print(str)

fourslist = []

for each in range(4, len(str)):
    fourletters = str[(each-4):each]
    fourslist.append(fourletters)

print(fourslist)

for every in fourslist:
    makeset = set(every)
    # print(makeset)
    # print(fourslist.index(every))
    nth = fourslist.index(every)
    if len(makeset) != 4:
        continue
    else:
        count = nth + 4
        print(f"part one: {count}")
        break

# part two
with open ("day06.txt") as buffer:
    str = buffer.read().strip()

fourslist = []

for each in range(14, len(str)):
    fourletters = str[(each-14):each]
    fourslist.append(fourletters)

print("\n\n\n\n", fourslist)

for every in fourslist:
    makeset = set(every)
    # print(fourslist.index(every))
    # nth = fourslist.index(every)
    if len(makeset) != 14:
        continue
    else:
        count = nth + 14
        print(f"part two: {count}")
        break

## Source: got the idea of solving through application of sets from: https://github.com/PodolskiBartosz/advent-of-code-2022/blob/main/day-6/main.py