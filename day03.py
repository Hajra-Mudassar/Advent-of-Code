with open ("day03.txt") as rucksacks:
    mainlist = [sack for sack in rucksacks.read().strip().split("\n")]

#pairing up priorities with letters
import string
alph = list(string.ascii_letters)
print(alph)
dict = {}
n = 1
for i in alph:
    dict[i] = n
    n += 1
    length = len(alph)
    l = 0
    while l < length:
        l += 1
print(dict)

#looping over the data, dividing strings into sets, finding common letter and adding its priority into a main variable
priority = 0
for eachsack in mainlist:
    s = eachsack
    a = s[0:len(s)//2]
    b = s[len(s)//2:len(s)]
    seta = set(a)
    setb = set(b)
    for i in alph:
        if i in seta and i in setb:
            priority += dict[i]

print(f"part one answer: {priority}")

# part two
# applying a for loop pver a range of 3 on the mainlist so one group pf three eleves sack is scanned and applying another index called everythirdsack to iterate within one group
prioritytwo = 0
everythirdsack = 3
for everysack in range(0, len(mainlist), 3):
    onegroup = mainlist[everysack:everythirdsack]
    everythirdsack += 3
    for i in alph:
        if i in onegroup[0] and i in onegroup[1] and i in onegroup[2]:
            prioritytwo += dict[i]

print(f"part two answer: {prioritytwo}")

