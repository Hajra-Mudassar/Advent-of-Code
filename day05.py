with open ("day05.txt") as stacks:
    a, b = (each.splitlines() for each in stacks.read().split("\n\n"))

print(f"a: {a},\nb: {b}")

# making the nine initial stacks manually
stack0 = [' ']
stack1 = ['W', 'R', 'F']
stack2 = ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P']
stack3 = ['P', 'M', 'Z', 'N', 'L']
stack4 = ['J', 'C', 'H', 'R']
stack5 = ['C', 'P', 'G', 'H', 'Q', 'T', 'B']
stack6 = ['G', 'C', 'W', 'L', 'F', 'Z']
stack7 = ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C']
stack8 = ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C']
stack9 = ['J', 'W', 'H', 'G', 'R', 'S', 'V']
listofstacks = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
print(listofstacks)

instructionlist = []
for i in b:
    instructionlist.append(i.strip().split(" "))

for eachins in instructionlist:
    howmany = int(eachins[1])
    initial = int(eachins[3])
    destin = int(eachins[5])

    for i in range(howmany):
        removed = listofstacks[initial].pop()
        listofstacks[destin].append(removed)

topmost = stack1[-1], stack2[-1], stack3[-1], stack4[-1], stack5[-1], stack6[-1], stack7[-1], stack8[-1], stack9[-1]
stringform = ''
for each in topmost:
    stringform = stringform + each

print(f"\nAnswer to part one: {stringform}")

# PART TWO
with open ("day05.txt") as stacks:
    a, b = (each.splitlines() for each in stacks.read().split("\n\n"))

print(f"\n\na: {a},\nb: {b}")

# making the nine initial stacks manually
stack0 = [' ']
stack1 = ['W', 'R', 'F']
stack2 = ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P']
stack3 = ['P', 'M', 'Z', 'N', 'L']
stack4 = ['J', 'C', 'H', 'R']
stack5 = ['C', 'P', 'G', 'H', 'Q', 'T', 'B']
stack6 = ['G', 'C', 'W', 'L', 'F', 'Z']
stack7 = ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C']
stack8 = ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C']
stack9 = ['J', 'W', 'H', 'G', 'R', 'S', 'V']
listofstacks = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
print(listofstacks)

instructionlist = []
for i in b:
    instructionlist.append(i.strip().split(" "))

for eachins in instructionlist:
    howmany = int(eachins[1])
    initial = int(eachins[3])
    destin = int(eachins[5])

    listone = listofstacks[destin]
    listtwo = listofstacks[initial]
    listthree = listtwo[-howmany:]
    for i in listthree:
        listtwo.pop()
    for i in listthree:
         listone.append(i)

topmost = stack1[-1], stack2[-1], stack3[-1], stack4[-1], stack5[-1], stack6[-1], stack7[-1], stack8[-1], stack9[-1]
stringform = ''
for each in topmost:
        stringform = stringform + each

print(f"\nAnswer to part two: {stringform}")



