from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr

with open("day21.txt") as yells:
    monkeylist = yells.read().strip().split("\n")

monkeydetails = {}
for eachmonkey in monkeylist:
    nameandyell = eachmonkey.split(" ")
    monkeyname = nameandyell[0][:-1]

    if len(nameandyell) == 2:
        monkeydetails[monkeyname] = int(nameandyell[1])
    else:
        monkeydetails[monkeyname] = nameandyell[1:]

def yellfunction(monkeyname):
    monkeysyell = monkeydetails[monkeyname]
    if not isinstance(monkeysyell, int):
        parts = monkeydetails[monkeyname]
        left = yellfunction(parts[0])
        operataion = parts[1]
        right = yellfunction(parts[2])

        if operataion == '+':
            yell = left + right
            return yell
        elif operataion == '-':
            yell = left - right
            return yell
        elif operataion == '*':
            yell = left * right
            return yell
        elif operataion == '/':
            yell = left // right
            return yell
    elif isinstance(monkeysyell, int):
        return monkeysyell

rootsyell = yellfunction("root")
print(f"part one answer: {rootsyell}")

### PART TWO

with open("day21.txt") as yells:
    monkeylist = yells.read().strip().split("\n")

monkeydetails = {}
human = symbols("humn")

for eachmonkey in monkeylist:
    yell = eachmonkey.split(" ")

    monkeyname = yell[0][:-1]

    if len(yell) == 2:
        monkeydetails[monkeyname] = int(yell[1])
    else:
        monkeydetails[monkeyname] = yell[1:]

def yellfunction(monkeyname):
    if monkeyname== "humn":
        return human

    if isinstance(monkeydetails[monkeyname], int):
        return monkeydetails[monkeyname]

    thismonkeysyell = monkeydetails[monkeyname]

    leftside = yellfunction(thismonkeysyell[0])
    rightside = yellfunction(thismonkeysyell[2])

    return parse_expr(f"({leftside}){thismonkeysyell[1]}({rightside})")

firstinroot = yellfunction(monkeydetails["root"][0])
secondinroot = yellfunction(monkeydetails["root"][2])
print(f"{firstinroot} should be equal to {secondinroot}")
print(solve_linear(firstinroot, secondinroot))
myyell = solve_linear(firstinroot, secondinroot)[1]
print(f"part two : {myyell}")

## Source: https://www.youtube.com/watch?v=wKaQxkxv-vM&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=6