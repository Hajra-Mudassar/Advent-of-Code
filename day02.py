with open("day02.txt") as rps:
   str = rps.read().strip().split("\n")

print(str)
total = 0
totalsecond = 0
for i in str:
    if i == 'A X':
            score = 4
            secondscore = 3
    elif i == 'A Y':
            score = 8
            secondscore = 4
    elif i == 'A Z':
            score = 3
            secondscore = 8
    elif i == 'B X':
            score = 1
            secondscore = 1
    elif i == 'B Y':
            score = 5
            secondscore = 5
    elif i == 'B Z':
            score = 9
            secondscore = 9
    elif i == 'C X':
            score = 7
            secondscore = 2
    elif i == 'C Y':
            score = 2
            secondscore = 6
    elif i == 'C Z':
            score = 6
            secondscore = 7
    total += score
    totalsecond += secondscore
    i =+ 1

print(f"The total score: {total} and total for second part is: {totalsecond}")
