with open ("day10.txt") as ourfile:
    main = ourfile.read().strip().split("\n")

print(main)
cyclecount = 0

for20th = 0
for60th = 0
for100th = 0
for140th = 0
for180th = 0
for220th = 0

regvalue = 1
for each in main:
    #print(each)
    if "noop" in each:
        cyclecount += 1
        if cyclecount == 20:
            for20th += regvalue * cyclecount
        if cyclecount == 60:
            for60th += regvalue * cyclecount
        if cyclecount == 100:
            for100th += regvalue * cyclecount
        if cyclecount == 140:
            for140th += regvalue * cyclecount
        if cyclecount == 180:
            for180th += regvalue * cyclecount
        if cyclecount == 220:
            for220th += regvalue * cyclecount

    elif "addx" in each:
        for every in range(2):
            cyclecount += 1
            if cyclecount == 20:
                for20th += regvalue * cyclecount
            if cyclecount == 60:
                for60th += regvalue * cyclecount
            if cyclecount == 100:
                for100th += regvalue * cyclecount
            if cyclecount == 140:
                for140th += regvalue * cyclecount
            if cyclecount == 180:
                for180th += regvalue * cyclecount
            if cyclecount == 220:
                for220th += regvalue * cyclecount
        x = each.split()
        regvalue += int(x[1])

Totalstrength = for20th + for60th + for100th + for140th + for180th + for220th

print(f"Total cycles: {cyclecount}")

print(f"\nTotal signal strength for part one is: {Totalstrength}")