with open("day01.txt") as elfs:
    lista = [value for value in elfs.read().strip().split("\n")]

listb = []
calorie = 0
for each in lista:
    if each == '':
        listb.append(calorie)
        calorie = 0
    else:
        integer = int(each)
        calorie += integer

print(f"Maximum calories carried by an elf are: {max(listb)}")

maxim = max(listb)
listb.remove(maxim)

print(f"Second max value:{max(listb)} ")

maximb = max(listb)
listb.remove(maximb)

print(f"Third max value:{max(listb)} ")

maximc = max(listb)
total = maxim+maximb+maximc
print(f"Total calories carried by the three Elves are: {total}")

