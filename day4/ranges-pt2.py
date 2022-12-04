data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day4\data.txt","r").readlines()
rangesList = []
pairsList = []
tempPair = []
score = 0
for x in data:
    ranges = x.strip().split(",")
    for y in ranges:
        y = y.split("-")
        rangesList.append(y)
for x in range(0, len(rangesList), 2):
    pairsList.append(rangesList[x:x+2])
for x in pairsList:
    if (int(x[0][1]) < int(x[1][0])) or (int(x[0][0]) > int(x[1][1])):
        score += 1
print(len(data) - score)