from functools import cmp_to_key

with open("day13.txt") as signal:
    signallist = signal.read().strip().split("\n\n")
print(signallist)

def compare(first, second):
    if type(first) == int:
        if type(second) == list:
            first = [first]

    if type(first) == list:
        if type(second) == int:
            second = [second]

    if type(first) == int:
        if type(first) == int:
            if first == second:
                return 0
            if first < second:
                return 1
            elif first > second:
                return -1

    if type(first) == list:
        if type(first) == list:
            turninlist = 0
            while turninlist < len(first) and turninlist < len(second):
                comparingboth = compare(first[turninlist], second[turninlist])
                if comparingboth == 1:
                    return 1
                if comparingboth == -1:
                    return -1
                turninlist += 1

        if turninlist == len(first):
            if len(first) == len(second):
                return 0
            else:
                return 1
        elif turninlist == len(second):
            return -1

sumindices = []

for indexofcomparison, eachcomparison in enumerate(signallist):
    firstline = eval(eachcomparison.split("\n")[0])
    secondline = eval(eachcomparison.split("\n")[1])
    if compare(firstline, secondline) == 1:
        indexinreal = indexofcomparison + 1
        sumindices.append(indexinreal)

print(f"part one answer: {sum(sumindices)}")

### PART TWO

with open("day13.txt") as distress:
    signallist = distress.read().strip().replace("\n\n", "\n").split("\n")

decodelist = list(map(eval, signallist))
decodelist.append([[2]])
decodelist.append([[6]])
decodelist = sorted(decodelist, key=cmp_to_key(compare), reverse=True)


for indexofcomparison, eachcomparison in enumerate(decodelist):
    if eachcomparison == [[2]]:
        indexinreal = indexofcomparison + 1
        firstindice = indexinreal
    if eachcomparison == [[6]]:
        indexinreal = indexofcomparison + 1
        secondindice = indexinreal

print(f"part two answer: {firstindice * secondindice}")

### SOURCE: https://www.youtube.com/watch?v=dksdTAYB_X8&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=13