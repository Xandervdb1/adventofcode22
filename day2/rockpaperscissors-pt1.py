data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day2\data.txt","r").readlines()
score = 0
choiceScore = 0
opponent = ""
choice = ""
scoreList = []
def checkWin():
    if (opponent == "rock" and choice == "rock") or (opponent == "paper" and choice == "paper") or (opponent == "scissors" and choice == "scissors"):
        score = 3
        return score
    elif (opponent == "rock" and choice == "paper") or (opponent == "paper" and choice == "scissors") or (opponent == "scissors" and choice == "rock"):
        score = 6
        return score
    elif (opponent == "rock" and choice == "scissors") or (opponent == "paper" and choice == "rock") or (opponent == "scissors" and choice == "paper"):
        score = 0
        return score
for x in data:
    raw = x.strip().replace(" ", "")
    for y in raw:
        if y == "A":
            opponent = "rock"
        elif y == "B":
            opponent = "paper"
        elif y == "C":
            opponent = "scissors"
        elif y == "X":
            choice = "rock"
            choiceScore = 1
        elif y == "Y":
            choice = "paper"
            choiceScore = 2
        elif y == "Z":
            choice = "scissors"
            choiceScore = 3
    scoreList.append(checkWin() + choiceScore)
print(sum(scoreList))