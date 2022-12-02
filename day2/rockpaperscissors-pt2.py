data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day2\data.txt","r").readlines()
score = 0
choiceScore = 0
opponent = ""
outcome = ""
scoreList = []
def checkChoice():
    if outcome == "lose":
        score = 0
        if opponent == "rock":
            choiceScore = 3
        elif opponent == "paper":
            choiceScore = 1
        elif opponent == "scissors":
            choiceScore = 2
    elif outcome == "draw":
        score = 3
        if opponent == "rock":
            choiceScore = 1
        elif opponent == "paper":
            choiceScore = 2
        elif opponent == "scissors":
            choiceScore = 3
    elif outcome == "win":
        score = 6
        if opponent == "rock":
            choiceScore = 2
        elif opponent == "paper":
            choiceScore = 3
        elif opponent == "scissors":
            choiceScore = 1
    scoreList.append(score + choiceScore)         
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
            outcome = "lose"
        elif y == "Y":
            outcome = "draw"
        elif y == "Z":
            outcome = "win"
    checkChoice()
print(sum(scoreList))