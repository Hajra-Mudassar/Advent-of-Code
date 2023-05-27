with open("day09.txt") as directions:
    directionslist = directions.read().strip().split("\n")

headx = 0
heady = 0
tailx = 0
taily = 0

directionsdictionary = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}

donestates = set()
donestates.add((tailx, taily))
# adding 0,0 for tails position, so it isn't missed later

for each in directionslist:
    direction, howmuch = each.split(" ")
    howmuch = int(howmuch)
    headdirectionx, headdirectiony = directionsdictionary[direction]

    for everystep in range(howmuch):

        # updating heads position
        headx += headdirectionx
        heady += headdirectiony

        # if the difference of distance between the head and tail is less then or equal to 1, theyre touching, so pass, else process
        if (abs(headx - tailx) <= 1 and abs(heady - taily) <= 1):
            pass
        else:
            if headx == tailx:
                tailmovementx = 0
            else:
                tailmovementx = (headx - tailx) / abs(headx - tailx)
                # in each step, if the head moves, the tail is only going to move one step, so abs used
            if heady == taily:
                tailmovementy = 0
            else:
                tailmovementy = (heady - taily) / abs(heady - taily)

            # updating tails position
            tailx += tailmovementx
            taily += tailmovementy
        donestates.add((tailx, taily))

# print(donestates)
print(f"part one answer: {len(donestates)}")

### PART TWO

with open("day09.txt") as directions:
    directionslist = directions.read().strip().split("\n")

allnineknots = [[0, 0] for eachknot in range(10)]

directionsdictionary = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}

donestates = set()
donestates.add(tuple(allnineknots[-1]))
# adding 0,0 for tails position, so it isn't missed later

for each in directionslist:
    direction, howmuch = each.split(" ")
    howmuch = int(howmuch)
    headdirectionx, headdirectiony = directionsdictionary[direction]

    for everystep in range(howmuch):

        # updating heads position
        allnineknots[0][0] += headdirectionx
        allnineknots[0][1] += headdirectiony

        for each in range(1, 10):
            headx, heady = allnineknots[each - 1]
            tailx, taily = allnineknots[each]

            # if the difference of distance between the head and tail is less then or equal to 1, theyre touching, so pass, else process
            if (abs(headx - tailx) <= 1 and abs(heady - taily) <= 1):
                pass
            else:
                if headx == tailx:
                    tailmovementx = 0
                else:
                    tailmovementx = (headx - tailx) / abs(headx - tailx)
                    # in each step, if the head moves, the tail is only going to move one step, so abs used
                if heady == taily:
                    tailmovementy = 0
                else:
                    tailmovementy = (heady - taily) / abs(heady - taily)

                # updating tails position
                tailx += tailmovementx
                taily += tailmovementy

                allnineknots[each] = [tailx, taily]

                donestates.add(tuple(allnineknots[-1]))

# print(donestates)
print(f"part two answer: {len(donestates)}") 

### SOURCE: https://www.youtube.com/watch?v=QfSPVrWKGcU&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=14