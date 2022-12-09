myScore = 0

guide = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

LOSE = 1
DRAW = 2
WIN = 3

ROCK = 1
PAPER = 2
SCISSORS = 3


def playRound(round):
    global myScore
    oppPlay = guide.get(round[0])
    outcome = guide.get(round[1])

    if (outcome == WIN):
        myScore += 6
        if (oppPlay == SCISSORS):
            myScore += ROCK
        else:
            play = oppPlay + 1
            myScore += play
    elif (outcome == LOSE):
        if (oppPlay == ROCK):
            myScore += SCISSORS
        else:
            play = oppPlay - 1
            myScore += play
    else:
        myScore += DRAW + oppPlay


with open("Day2/Part2/strategy.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.split():
            round = line.split()
            playRound(round)
    print(myScore)
