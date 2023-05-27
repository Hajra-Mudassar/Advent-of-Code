from tqdm import tqdm

with open("day11.txt") as monkeybusiness:
    allmonkeys = monkeybusiness.read().strip()
    monkeyslist = allmonkeys.split("\n\n")

monkeydetails = []
class eachmonkey:
    def __init__(self, valuables, update, trufal):
        self.valuables = valuables
        self.update = update
        self.trufal = trufal
        self.inspects = 0

    def __str__(self):
        return f"{self.valuables}, {self.update}, {self.trufal}"


for everymonkey in monkeyslist:
    info = everymonkey.split("\n")
    valuables = list(map(int, info[1][2:].split(" ", 2)[2].split(", ")))
    update = info[2][2:].split(" ", 3)[3].split(" ")

    divisible = int(info[3][2:].split(" ")[-1])
    incasetrue = int(info[4][4:].split(" ")[-1])
    incasefalse = int(info[5][4:].split(" ")[-1])

    monkeydetails.append(eachmonkey(valuables, update, [divisible, incasetrue, incasefalse]))


numberofmonkeys = len(monkeydetails)
for i in range(20):
    for currentmonkey in range(numberofmonkeys):
        for eachvaluable in monkeydetails[currentmonkey].valuables:
            monkeydetails[currentmonkey].inspects += 1

            firstword = monkeydetails[currentmonkey].update[0]
            operation = monkeydetails[currentmonkey].update[1]
            secondword = monkeydetails[currentmonkey].update[2]
            if firstword == "old":
                if operation == "+":
                    eachvaluable = eachvaluable + int(secondword)
                else:
                    if secondword == "old":
                        eachvaluable = eachvaluable * eachvaluable
                    else:
                        eachvaluable = eachvaluable * int(secondword)
            eachvaluable = eachvaluable // 3

            divisible = monkeydetails[currentmonkey].trufal[0]
            incasetrue = monkeydetails[currentmonkey].trufal[1]
            incasefalse = monkeydetails[currentmonkey].trufal[2]
            if eachvaluable % divisible == 0:
                monkeydetails[incasetrue].valuables.append(eachvaluable)
            else:
                monkeydetails[incasefalse].valuables.append(eachvaluable)

        monkeydetails[currentmonkey].valuables = []

allinspections = []
for everymonkey in monkeydetails:
    allinspections.append(everymonkey.inspects)

firstmax = max(allinspections)
# print(firstmax)
allinspections.remove(firstmax)
secondmax = max(allinspections)
print(f"part one answer: {firstmax * secondmax}")


#### PART TWO


with open("day11.txt") as monkeybusiness:
    allmonkeys = monkeybusiness.read().strip()
    monkeyslist = allmonkeys.split("\n\n")

monkeydetails = []

class eachmonkey:
    def __init__(self, valuables, update, trufal):
        self.valuables = valuables
        self.update = update
        self.trufal = trufal
        self.inspects = 0

    def __str__(self):
        return f"{self.valuables}, {self.update}, {self.trufal}"


for everymonkey in monkeyslist:
    info = everymonkey.split("\n")
    valuables = list(map(int, info[1][2:].split(" ", 2)[2].split(", ")))
    update = info[2][2:].split(" ", 3)[3].split(" ")

    divisible = int(info[3][2:].split(" ")[-1])
    incasetrue = int(info[4][4:].split(" ")[-1])
    incasefalse = int(info[5][4:].split(" ")[-1])

    monkeydetails.append(eachmonkey(valuables, update, [divisible, incasetrue, incasefalse]))

mainmodulosum = 1
for monk in monkeydetails:
    mainmodulosum *= monk.trufal[0]

numberofmonkeys = len(monkeydetails)
for i in tqdm(range(10000)):
    for currentmonkey in range(numberofmonkeys):
        for eachvaluable in monkeydetails[currentmonkey].valuables:
            monkeydetails[currentmonkey].inspects += 1

            firstword = monkeydetails[currentmonkey].update[0]
            operation = monkeydetails[currentmonkey].update[1]
            secondword = monkeydetails[currentmonkey].update[2]
            if firstword == "old":
                if operation == "+":
                    eachvaluable = eachvaluable + int(secondword)
                else:
                    if secondword == "old":
                        eachvaluable = eachvaluable * eachvaluable
                    else:
                        eachvaluable = eachvaluable * int(secondword)
                eachvaluable = eachvaluable % mainmodulosum

            divisible = monkeydetails[currentmonkey].trufal[0]
            incasetrue = monkeydetails[currentmonkey].trufal[1]
            incasefalse = monkeydetails[currentmonkey].trufal[2]
            if eachvaluable % divisible == 0:
                monkeydetails[incasetrue].valuables.append(eachvaluable)
            else:
                monkeydetails[incasefalse].valuables.append(eachvaluable)

        monkeydetails[currentmonkey].valuables = []

allinspections = []
for everymonkey in monkeydetails:
    allinspections.append(everymonkey.inspects)

firstmax = max(allinspections)
# print(firstmax)
allinspections.remove(firstmax)
secondmax = max(allinspections)
print(f"part two answer: {firstmax * secondmax}")

### SOURCE: https://www.youtube.com/watch?v=63-uEScYUvM&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=14
