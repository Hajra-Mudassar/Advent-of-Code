from tqdm import tqdm

with open("day20.txt") as encr:
    mainlist = encr.read().strip().split("\n")
    idlist = list(enumerate(map(int, mainlist)))

# print(idlist)

lenghtoflist = len(idlist)
# print(lenghtoflist)
unchangedorder = idlist.copy()

for ind, val in tqdm(unchangedorder):
    for indextolook in range(lenghtoflist):
        if idlist[indextolook][0] == ind:
            index = indextolook
            break

    if idlist[index][1] == val:
        if val < 0:
            for each in range(-val):
                first = index
                second = (index - 1) % lenghtoflist
                if (0 <= first < lenghtoflist) and (0 <= second < lenghtoflist):
                    idlist[first], idlist[second] = idlist[second], idlist[first]
                index = (index - 1) % lenghtoflist
            else:
                continue

        if val > 0:
            for each in range(val):
                first = index
                second = (index + 1) % lenghtoflist
                if (0 <= first < lenghtoflist) and (0 <= second < lenghtoflist):
                    idlist[first], idlist[second] = idlist[second], idlist[first]
                index = (index + 1) % lenghtoflist

for zero in range(lenghtoflist):
    if idlist[zero][1] == 0:
        zeroindex = zero
        break

sumofall = 0
checkpoints = [1000, 2000, 3000]
for each in checkpoints:
    movedindex = (zeroindex + each) % lenghtoflist
    numberatcheckpoint = idlist[movedindex][1]
    sumofall += numberatcheckpoint

print(f"part one answer: {sumofall}")

### PART TWO ###

with open("day20.txt") as encr:
    mainlist = encr.read().strip().split("\n")
    part2list = list(map(int, mainlist))

    for eachnumber in range(len(part2list)):
        eachvalue = part2list[eachnumber] * 811589153
        part2list[eachnumber] = (eachnumber, eachvalue)

# print(part2list)
lenghtoflist2 = len(part2list)
part2unchangedorder = part2list.copy()

for i in tqdm(range(10)):
    for ind, val in tqdm(part2unchangedorder):
        for indextolook in range(lenghtoflist2):
            if part2list[indextolook][0] == ind:
                index = indextolook
                break

        if part2list[index][1] == val:
            val %= (lenghtoflist2 - 1)

            if val > 0:
                for each in range(val):
                    first = index
                    second = (index + 1) % lenghtoflist2
                    if (0 <= first < lenghtoflist2) and (0 <= second < lenghtoflist2):
                        part2list[first], part2list[second] = part2list[second], part2list[first]
                    index = (index + 1) % lenghtoflist2
    print(f"\nend of turn {i}")

for zero in range(lenghtoflist2):
    if part2list[zero][1] == 0:
        zeroindex = zero
        break

sumofallfor2 = 0
checkpoints = [1000, 2000, 3000]
for each in checkpoints:
    movedindex = (zeroindex + each) % lenghtoflist2
    numberatcheckpoint = part2list[movedindex][1]
    sumofallfor2 += numberatcheckpoint

print(f"part two answer: {sumofallfor2}")

### SOURCE: https://www.youtube.com/watch?v=QgS36OQxAgE&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=6

