data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day3\data.txt","r").readlines()
splitList = []
tempList = []
solution = []
def letterToNumber(letter):
    if letter.isupper():
        number = ord(letter) - 64 + 26
        return number
    else:
        number = ord(letter) - 96
        return number
for x in data:
    x.strip()
    firsthalf = slice(0, len(x)//2)
    lasthalf = slice(len(x)//2, len(x))
    tempList.append(x[firsthalf])
    tempList.append(x[lasthalf].strip())
    splitList.append(tempList.copy())
    tempList.clear()
for backpack in splitList:
    commonChar = ''.join(set(backpack[0]).intersection(backpack[1]))
    solution.append(letterToNumber(commonChar))
print(sum(solution))