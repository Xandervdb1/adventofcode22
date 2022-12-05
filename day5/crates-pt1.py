data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day5\data.txt","r").readlines()
amountOfStacks = 0
highestStack = 8
layers = []
rows = []
divRow = []
for x in data:
    x = x.strip()
    if x.startswith("1"):
        amountOfStacks = int(x[-1])
for x in data:
    y = x.strip()
    if y.startswith("1"):
        break
    else:
        layer = [x[i:i+4] for i in range(0, len(x), 4)]
        layers.append(layer)
for j in range(0, amountOfStacks):
    for i in range(0, highestStack):
        rows.append(layers[i][j])
for i in range(0, len(rows), highestStack):
    x = i
    divRow.append(rows[x:x+highestStack])
print(divRow)
for x in divRow:
    for i in range(0, highestStack):
        while("    " in divRow[i]):
            divRow[i].remove("    ")
        while("   \n" in divRow[i]):
            divRow[i].remove("   \n")
def moveBoxes(fromRow, toRow, amount):
    target = fromRow[0:int(amount)]
    for i in range(0, len(target)):
        toRow.insert(0, target[i])
        fromRow.pop(0)
for x in data:
    if x.startswith("move"):
        x = [int(s) for s in x.split() if s.isdigit()]
        fromRow = divRow[int(x[1])-1]
        toRow = divRow[int(x[2])-1]
        amount = x[0]
        moveBoxes(fromRow, toRow, amount)
for i in range(0, len(divRow)):
    print(divRow[i][0])
