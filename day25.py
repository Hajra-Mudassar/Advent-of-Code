with open("day25.txt") as code:
    fuelnumber = code.read().strip().split()

snafutodecimal = { '-': -1, '=': -2, '0': 0, '1': 1, '2': 2 }
decimaltosnafu = { 0: '0', 1: '1', 2: '2', -1: '-', -2: '=' }

def codetosnafu(decimals):
    snafucode = ""
    while decimals > 0:
        digit = ((decimals + 2) % 5) - 2
        snafudigit = decimaltosnafu[digit]
        snafucode += snafudigit
        decimals -= digit
        decimals //= 5
    return snafucode[::-1]

decstatement = 0
for eachfuel in fuelnumber:
    eachfuel = eachfuel[::-1]
    five = 1
    eachdigit = 0
    for digit in range(len(eachfuel)):
        mutipleoffive = five * snafutodecimal[eachfuel[digit]]
        eachdigit += mutipleoffive
        five *= 5
    decstatement += eachdigit

snafustatement = codetosnafu(decstatement)
print(f"answer: {snafustatement}")

### SOURCE: https://www.youtube.com/watch?v=emGvddhDsYA&list=PLsqh-jhhTL2-cJiIRlju1sQj0i_Sk9zmd&index=2