import numpy as np
from tqdm import tqdm

with open("day18.txt") as file:
    setslist = file.read().strip().split("\n")

print(setslist)

exposedsides = 0

viewedlist = []
for each in setslist:
    xposition, yposition, zposition = map(int, each.split(","))
    viewedlist.append((xposition, yposition, zposition))

print(viewedlist)

for xposition, yposition, zposition in viewedlist:
    mergedsides = 0
    currentcube = np.array((xposition,yposition, zposition))
    # print(f"the current cube is: {currentcube}")

    for eachside in range(3):

        onesidecheck = np.array([0, 0, 0])
        onesidecheck[eachside] = 1

        secondsidecheck = np.array([0, 0, 0])
        secondsidecheck[eachside] = -1

        # print(f"for {currentcube} the onesidechange is {onesidecheck} and secondsidechange is {secondsidecheck}")

        oneside = tuple(currentcube + onesidecheck)
        secondside = tuple(currentcube + secondsidecheck)

        if oneside in viewedlist:
            mergedsides += 1
        # print(f"for {currentcube} the oneside is {tuple(currentcube+onesidecheck)}")
        # print(f"covered here for {currentcube} is {mergedsides}")
        if secondside in viewedlist:
            mergedsides += 1
        # print(f"for {currentcube} the secondside is {tuple(currentcube+secondsidecheck)}")
        # print(f"covered here for {currentcube} is {mergedsides}")

    totalsidesofthiscube = 6 - mergedsides
    exposedsides += totalsidesofthiscube

print(f"answer for part one: {exposedsides}")

### PART TWO

with open("day18.txt") as file:
    setslist = file.read().strip().split("\n")

minimum = 0
maximum = 0

viewedsets = set()
for each in setslist:
    xposition, yposition, zposition = map(int, each.split(","))
    viewedsets.add((xposition, yposition, zposition))

    for every in [xposition, yposition, zposition]:
        minimum = min(minimum, every)
        maximum = max(maximum, every)

def fullyexterior(cube):
    alreadyvisited = set()
    listofcubes = [cube]

    while len(listofcubes) > 0:
        currentcube = listofcubes.pop()

        if currentcube in viewedsets:
            continue

        for eachside in range(3):
            if not (minimum <= currentcube[eachside] <= maximum):
                return True

        if currentcube in alreadyvisited:
            continue
        alreadyvisited.add(currentcube)

        for eachside in range(3):
            onesidecheck = np.array([0, 0, 0])
            onesidecheck[eachside] = 1

            secondsidecheck = np.array([0, 0, 0])
            secondsidecheck[eachside] = -1

            oneside = tuple(currentcube + onesidecheck)
            secondside = tuple(currentcube + secondsidecheck)

            listofcubes.append(oneside)
            listofcubes.append(secondside)
    return False


exteriorsurface = 0

for xposition, yposition, zposition in tqdm(viewedsets):
    currentcube = np.array((xposition, yposition, zposition))

    for eachside in range(3):
        onesidecheck = np.array([0, 0, 0])
        onesidecheck[eachside] = 1

        secondsidecheck = np.array([0, 0, 0])
        secondsidecheck[eachside] = -1

        for eachcube in [tuple(currentcube + onesidecheck), tuple(currentcube + secondsidecheck)]:
            exteriorsurface += fullyexterior(eachcube)

print(f"part two: {exteriorsurface}")

### SOURCE: https://www.youtube.com/watch?v=xPIMCrbRPOI&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=7