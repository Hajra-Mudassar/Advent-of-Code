import string
import heapq

with open("day12.txt") as map:
    mainlist = map.read().strip().split()

alph = list(string.ascii_lowercase)
print(alph)

characterslist = []
for each in mainlist:
    characterslist.append(each)

rowsinmap = len(characterslist)
colsinmap = len(characterslist[0])

for row in range(rowsinmap):
    for col in range(colsinmap):
        currentlocation = characterslist[row][col]
        if currentlocation == 'E':
            destin = row, col
        elif currentlocation == 'S':
            initial = row, col

def parsingneighbours(row, col):
    for rowneighbour, colneighbour in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        neighbourone = row + rowneighbour
        neighbourtwo = col + colneighbour
        # print(neighbourone, neighbourtwo)

        if not (0 <= neighbourone and neighbourone < rowsinmap and 0 <= neighbourtwo and neighbourtwo < colsinmap):
            continue

        nextelevation = indexing(characterslist[neighbourone][neighbourtwo])
        currentelevation = indexing(characterslist[row][col]) + 1

        if nextelevation <= currentelevation:
            yield neighbourone, neighbourtwo

def indexing(letter):
    if letter in alph:
        return string.ascii_lowercase.index(letter)
    elif letter == 'E':
        return 25
    elif letter == 'S':
        return 0

alreadyvisited = []
for each in range(rowsinmap):
    alreadyvisited.append([False] * colsinmap)

currentinfo = [(0, initial[0], initial[1])]

while True:
    reqsteps, row, col = heapq.heappop(currentinfo)

    if alreadyvisited[row][col]:
        continue
    alreadyvisited[row][col] = True

    if (row, col) == destin:
        print(f"part one: {reqsteps}")
        break

    for eachrow, eachcol in parsingneighbours(row, col):
        heapq.heappush(currentinfo, (reqsteps + 1, eachrow, eachcol))

### part two

with open("day12.txt") as map:
    mainlist = map.read().strip().split()

alph = list(string.ascii_lowercase)
print(alph)

characterslist = []
for each in mainlist:
    characterslist.append(each)

rowsinmap = len(characterslist)
colsinmap = len(characterslist[0])

for row in range(rowsinmap):
    for col in range(colsinmap):
        currentlocation = characterslist[row][col]
        if currentlocation == 'E':
            destin = row, col

def parsingneighbours(row, col):
    for rowneighbour, colneighbour in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        neighbourone = row + rowneighbour
        neighbourtwo = col + colneighbour
        # print(neighbourone, neighbourtwo)

        if not (0 <= neighbourone and neighbourone < rowsinmap and 0 <= neighbourtwo and neighbourtwo < colsinmap):
            continue

        currentelevation = indexing(characterslist[neighbourone][neighbourtwo])
        nextelevation = indexing(characterslist[row][col]) - 1

        if currentelevation >= nextelevation:
            yield neighbourone, neighbourtwo


def indexing(letter):
    if letter in alph:
        return string.ascii_lowercase.index(letter)
    elif letter == 'E':
        return 25

alreadyvisited = []
for each in range(rowsinmap):
    alreadyvisited.append([False] * colsinmap)

info = [(0, destin[0], destin[1])]

while True:
    reqsteps, row, col = heapq.heappop(info)

    if alreadyvisited[row][col]:
        continue
    alreadyvisited[row][col] = True

    if indexing(characterslist[row][col]) == 0:
        print(f"part two: {reqsteps}")
        break

    for eachrow, eachcol in parsingneighbours(row, col):
        heapq.heappush(info, (reqsteps + 1, eachrow, eachcol))

# SOURCE: https://www.youtube.com/watch?v=sBe_7Mzb47Y&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd
