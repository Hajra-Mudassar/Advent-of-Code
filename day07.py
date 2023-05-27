from collections import defaultdict

with open("day07.txt") as terminaloutput:
    listofcommands = ("\n" + terminaloutput.read().strip()).split("\n$ ")[1:]

print(listofcommands)
subdirectories = defaultdict(list)
dirsize = defaultdict(int)
pathofdirectories = []

# main function to go through the inpput and update the directories accordingly
def updates(listofcommands):
    eachstatement = listofcommands.split("\n")
    operation = eachstatement[0]
    contents = eachstatement[1:]

    twosteps = operation.split(" ")
    commandinop = twosteps[0]

    # for the command
    if commandinop == "cd":
        if twosteps[1] == "..":
            pathofdirectories.pop()
        else:
            pathofdirectories.append(twosteps[1])
        return

    # for the output of that command (if any)
    path = "/".join(pathofdirectories)

    if commandinop == "ls":
        totalsizeofdir = []
        for eachline in contents:
            if eachline.startswith("dir"):
                directoryname = eachline.split(" ")[1]
                newdirectory = path + "/" + directoryname
                subdirectories[path].append(newdirectory)
            else:
                sizeoffile = int(eachline.split(" ")[0])
                totalsizeofdir.append(sizeoffile)

        dirsize[path] = sum(totalsizeofdir)


# recursive function for sizes inclusing subdirectories
def recursiveforsizeofsubdir(path):
    totalsize = dirsize[path]
    for subdir in subdirectories[path]:
        totalsize += recursiveforsizeofsubdir(subdir)
    return totalsize

for eachcommand in listofcommands:
    updates(eachcommand)

# for directories of only up to 100000 size
sizeofselecteddir = 0
for path in dirsize:
    if recursiveforsizeofsubdir(path) <= 100000:
        sizeofselecteddir += recursiveforsizeofsubdir(path)

print(f"answer for part one: {sizeofselecteddir}")

## PART TWO

freespace = 70000000 - recursiveforsizeofsubdir("/")
neededspace = 30000000 - freespace

deletedir = []
for path in dirsize:
    size = recursiveforsizeofsubdir(path)
    if size >= neededspace:
        deletedir.append(size)

selectedfordeletion = min(deletedir)

print(f"answer for part two : {selectedfordeletion}")

### SOURCE: https://www.youtube.com/watch?v=YLHPABNNgZU&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=18
