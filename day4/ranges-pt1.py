data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day4\data.txt","r").readlines()
rangesList = []
pairsList = []
tempPair = []
score = 0
solutions = []
for x in data:
    ranges = x.strip().split(",")
    for y in ranges:
        y = y.split("-")
        rangesList.append(y)
for x in range(0, len(rangesList), 2):
    pairsList.append(rangesList[x:x+2])
for x in pairsList:
    if ((x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) or (x[0][0] <= x[1][0] and x[0][1] >= x[1][1])):
        solutions.append(True)
        score += 1
    else:
        solutions.append(False)
print(solutions)
print(score)