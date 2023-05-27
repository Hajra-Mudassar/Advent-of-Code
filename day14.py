with open("day14.txt") as sand:
    sandlist = sand.read().strip().split("\n")

rockorsand = set()
for eachpath in sandlist:
    pathpoints = eachpath.split(" -> ")
    xandydirection = []
    for eachpoint in pathpoints:
        bothxy = list(map(int, eachpoint.split(",")))
        x = bothxy[0]
        y = bothxy[1]
        xandydirection.append((x, y))

    for eachpoint in range(1, len(xandydirection)):
        currentx, currenty = xandydirection[eachpoint]
        prevpoint = eachpoint - 1
        prevx, prevy = xandydirection[prevpoint]

        if currenty != prevy and currentx == prevx:
            lowesty = min(currenty, prevy)
            highesty = max(currenty, prevy) + 1
            for eachy in range(lowesty, highesty):
                rockorsand.add((currentx, eachy))
        elif currentx != prevx and currenty == prevy:
            lowestx = min(currentx, prevx)
            highestx = max(currentx, prevx) + 1
            for eachx in range(lowestx, highestx):
                rockorsand.add((eachx, currenty))

allverticalsfilled = []
for eachverticalfilled in rockorsand:
    allverticalsfilled.append(eachverticalfilled[1])
lastfilledverticalposition = max(allverticalsfilled)

def fallingsand():
    pointsx, pointsy = 500, 0
    while pointsy <= lastfilledverticalposition:
        downposition = (pointsx, pointsy + 1)
        leftposition = (pointsx - 1, pointsy + 1)
        rightposition = (pointsx + 1, pointsy + 1)
        if downposition not in rockorsand:
            pointsy += 1
            continue
        elif leftposition not in rockorsand:
            pointsx -= 1
            pointsy += 1
            continue
        elif rightposition not in rockorsand:
            pointsx += 1
            pointsy += 1
            continue
        newsand = (pointsx, pointsy)
        rockorsand.add(newsand)
        return True

    return False

totalsand = 0
while True:
    if fallingsand() == True:
        totalsand += 1
    elif fallingsand() == False:
        break
print(f"part one answer: {totalsand}")

### PART TWO

with open("day14.txt") as sand:
    sandlist = sand.read().strip().split("\n")

rockorsand = set()
for eachpath in sandlist:
    pathpoints = eachpath.split(" -> ")
    xandydirection = []
    for eachpoint in pathpoints:
        bothxy = list(map(int, eachpoint.split(",")))
        x = bothxy[0]
        y = bothxy[1]
        xandydirection.append((x, y))

    for eachpoint in range(1, len(xandydirection)):
        currentx, currenty = xandydirection[eachpoint]
        prevpoint = eachpoint - 1
        prevx, prevy = xandydirection[prevpoint]

        if currenty != prevy and currentx == prevx:
            lowesty = min(currenty, prevy)
            highesty = max(currenty, prevy) + 1
            for eachy in range(lowesty, highesty):
                rockorsand.add((currentx, eachy))
        elif currentx != prevx and currenty == prevy:
            lowestx = min(currentx, prevx)
            highestx = max(currentx, prevx) + 1
            for eachx in range(lowestx, highestx):
                rockorsand.add((eachx, currenty))

allverticalsfilled = []
for eachverticalfilled in rockorsand:
    allverticalsfilled.append(eachverticalfilled[1])
lastfilledverticalposition = max(allverticalsfilled)

def fallingsand():
    pointsx, pointsy = 500, 0

    if (pointsx, pointsy) in rockorsand:
        return(pointsx, pointsy)

    while pointsy <= lastfilledverticalposition:
        downposition = (pointsx, pointsy + 1)
        leftposition = (pointsx - 1, pointsy + 1)
        rightposition = (pointsx + 1, pointsy + 1)
        if downposition not in rockorsand:
            pointsy += 1
            continue
        elif leftposition not in rockorsand:
            pointsx -= 1
            pointsy += 1
            continue
        elif rightposition not in rockorsand:
            pointsx += 1
            pointsy += 1
            continue
        break

    return (pointsx, pointsy)

totalsanduntilallfilled = 0
while True:
    lastfilledx = fallingsand()[0]
    lastfilledy = fallingsand()[1]
    totalsanduntilallfilled += 1
    rockorsand.add((lastfilledx, lastfilledy))

    if (lastfilledx, lastfilledy) == (500, 0):
        break

print(f"part two answer: {totalsanduntilallfilled}")

### SOURCE: https://www.youtube.com/watch?v=lL2enOcBHVg&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=11