data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day6\data.txt","r").readlines()
uniqueCharacters = 4
score = uniqueCharacters
def grabFourFirst():
    firstFour = []
    for i in range(0,uniqueCharacters):
        firstFour.append(data[0][i])
    data[0] = data[0][uniqueCharacters:]
    return firstFour
def checkUnique(list):
    if (len(set(list)) == len(list)):
        return True
def moveLetter():
    checkList.append(data[0][0])
    checkList.pop(0)
    data[0] = data[0][1:]
checkList = grabFourFirst()
if checkUnique(checkList):
    print(score)
else:
    for i in range(0, len(data[0])):
        moveLetter()
        score += 1
        if checkUnique(checkList):
            print(score)
            break