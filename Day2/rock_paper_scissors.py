oppScore = 0
myScore = 0

guide = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}


def playRound(round):
    opp = guide.get(round[0])
    myp = guide.get(round[1])

    global oppScore
    global myScore
    oppScore += opp
    myScore += myp

    if (opp == myp):
        oppScore += 3
        myScore += 3
    elif (abs(opp-myp) > 1):
        if (opp > myp):
            myScore += 6
        else:
            oppScore += 6
    elif (opp > myp):
        oppScore += 6
    else:
        myScore += 6


with open("Day2/strategy.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.split():
            round = line.split()
            playRound(round)
    print("Opponents Score: " + str(oppScore))
    print("Your Score: " + str(myScore))
