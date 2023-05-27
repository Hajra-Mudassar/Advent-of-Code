## NO SPACE LEFT ON DEVICE
# find directories with size<100000 and sum of all

## split input, intro defaultdicts, two functions, main loop

from collections import defaultdict

with open("day07.txt") as terminaloutput:
    listofcommands = ("\n" + terminaloutput.read().strip()).split("\n$ ")[1:]

print(listofcommands)

## default dict: to not have to initialize all values for the dicts, auto initialises to zero
subdirectories = defaultdict(list)
dirsize = defaultdict(int)

## to maintain our current path in this path variable
pathofdirectories = []

# main function to go through the input and update the directories accordingly
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

    # turn list which contains parent directories into a giant string that represents our current path, useful for storing stuff inside out dicts
    path = "/".join(pathofdirectories)

    # for the output of that command (if any)
    if commandinop == "ls":
        totalsizeofdir = []
        for eachline in contents:

        ## when its a subdir, we add to children map: subdirectories dict by:
        ## create new path by adding / and dir name to path and to children of current path
            if eachline.startswith("dir"):
                directoryname = eachline.split(" ")[1]
                newdirectory = path + "/" + directoryname
                subdirectories[path].append(newdirectory)
            else:
                sizeoffile = int(eachline.split(" ")[0])
                totalsizeofdir.append(sizeoffile)

        dirsize[path] = sum(totalsizeofdir)

# recursive function for sizes including subdirectories
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

## freespace and to-delete space calc, min of all selected dirs is ans

freespace = 70000000 - recursiveforsizeofsubdir("/")
neededspace = 30000000 - freespace

## contains all directories suitable for deletion
deletedir = []
for path in dirsize:
    size = recursiveforsizeofsubdir(path)
    if size >= neededspace:
        deletedir.append(size)

# making sure we free up as little space as possible 
selectedfordeletion = min(deletedir)

print(f"answer for part two : {selectedfordeletion}")

### SOURCE: https://www.youtube.com/watch?v=YLHPABNNgZU&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=18
