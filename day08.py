with open ("day08.txt") as files:
    all = files.read().strip().split()

print(all)

### Removing the outermost visible rows of trees

numcolumns = len(all[0])
numrows = len(all)
# print(numrows, numcolumns)

innervisible = []
scenicscorelist = []

for eachrow in range(1, numrows-1):
    for eachcol in range(1, numcolumns-1):
        currenttree = all[eachrow][eachcol]
        # print(f"\n{currenttree}")

        leftfromtree = [all[eachrow][eachcol-i] for i in range(1, eachcol+1)]
        # print(f"\nleft from {currenttree} is : {leftfromtree}")
        leftscore = []
        for each in leftfromtree:
            if currenttree > each:
                leftscore.append(each)
            elif currenttree == each or currenttree < each:
                leftscore.append(each)
                break
        # print(f"the leftscore for {currenttree} is {len(leftscore)}")

        rightfromtree = [all[eachrow][eachcol+i] for i in range(1, numcolumns-eachcol)]
        # print(f"\nright from {currenttree} is : {rightfromtree}")
        rightscore = []
        for each in rightfromtree:
            if currenttree > each:
                rightscore.append(each)
            elif currenttree == each or currenttree < each:
                rightscore.append(each)
                break
        # print(f"the rightscore for {currenttree} is {len(rightscore)}")

        northfromtree = [all[eachrow-i][eachcol] for i in range(1, eachrow+1)]
        # print(f"\nnorth from {currenttree} is : {northfromtree}")
        northscore = []
        for each in northfromtree:
            if currenttree > each:
                northscore.append(each)
            elif currenttree == each or currenttree < each:
                northscore.append(each)
                break
        # print(f"the northscore for {currenttree} is {len(northscore)}")

        southfromtree = [all[eachrow+i][eachcol] for i in range(1, numrows-eachrow)]
        # print(f"\nsouth from {currenttree} is : {southfromtree}")
        southscore = []
        for each in southfromtree:
            if currenttree > each:
                southscore.append(each)
            elif currenttree == each or currenttree < each:
                southscore.append(each)
                break
        # print(f"the southscore for {currenttree} is {len(southscore)}")

        if currenttree > max(leftfromtree) or currenttree > max(rightfromtree) or currenttree > max(southfromtree) or currenttree > max(northfromtree):
            innervisible.append(currenttree)
        # print(f"\ninnervis: {innervisible}")

        totalscoreofcurrent = (len(leftscore)) * (len(rightscore)) * (len(northscore)) * (len(southscore))
        scenicscorelist.append(totalscoreofcurrent)
        # print(f"totalscoreofthisthree = {totalscoreofcurrent}")

### Visible trees separated, where 4 corners added in rows so removed in columns

outervisible = (numrows * 2) + ((numcolumns * 2) - 4)
# print(outervisible)
innervis = len(innervisible)
print(scenicscorelist)

totalvisible = outervisible + innervis
print(f"part one: {totalvisible}")
print(f"part two: {max(scenicscorelist)}")

### HELP SOURCE for part one list comprehensions: https://www.youtube.com/watch?v=o6KVs1EgAYk&list=PLFxlTcXTtPh-IbUalsqz-Ad7OPy7Yb0uf&index=12

