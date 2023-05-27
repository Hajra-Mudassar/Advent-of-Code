with open("day15.txt") as signals:
    locationslist = signals.read().strip().split("\n")

sensorslist = []
beaconslist = []

## Parsing the input in order to separate sensor and beacon coordinates
for eachloc in locationslist:
    values = eachloc.split(" ")
    sensorx = int(values[2][2:-1])
    sensory = int(values[3][2:-1])
    beaconx = int(values[8][2:-1])
    beacony = int(values[9][2:])

    sensorslist.append((sensorx, sensory))
    beaconslist.append((beaconx, beacony))

# setting limit and finding no beacon zones on it
limitline = 2000000
manhattendistancelist = []
nobeaconzones = []

for indexofsensor, thissensor in enumerate(sensorslist):
    # distances between sensors and beacons
    eachsensor = sensorslist[indexofsensor]
    itsbeacon = beaconslist[indexofsensor]
    distancebetween = abs(eachsensor[0] - itsbeacon[0]) + abs(eachsensor[1] - itsbeacon[1])
    manhattendistancelist.append(distancebetween)

    # determining all beacon positions on limit line
    beaconzones = []
    for eachbeacon in beaconslist:
        xofbeacon = eachbeacon[0]
        yofbeacon = eachbeacon[1]
        if yofbeacon == limitline:
            beaconzones.append(xofbeacon)

    # calculation of the total length of no beacon zone of every sensor on the limit line
    interval1sidelen = manhattendistancelist[indexofsensor] - abs(thissensor[1] - limitline)
    if interval1sidelen <= 0:
        continue
    totallengthofinterval = (thissensor[0] - interval1sidelen, thissensor[0] + interval1sidelen)
    nobeaconzones.append(totallengthofinterval)

# determining the ends of no beacon zones on limit line

maxintervallimit = []
for eachinterval in nobeaconzones:
    maxintervallimit.append(eachinterval[1])
limitlinemaxx = max(maxintervallimit) + 1

minintervallimit = []
for eachinterval in nobeaconzones:
    minintervallimit.append(eachinterval[0])
limitlineminx = min(minintervallimit)

# checking if x of a beacon exists within no beacon intervals, if it does then incrementing one on answer

nobeaconpositions = 0
for everyxonlimit in range(limitlineminx, limitlinemaxx):
    if everyxonlimit in beaconzones:
        continue

    for leftendofinterval, rightendofinterval in nobeaconzones:
        if leftendofinterval <= everyxonlimit <= rightendofinterval:
            nobeaconpositions += 1
            break

print(f"part one: {nobeaconpositions}")

### SOURCE: https://www.youtube.com/watch?v=w7m48_uCvWI&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=10