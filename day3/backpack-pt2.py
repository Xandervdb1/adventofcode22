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
for x in range(0, len(data), 3):
    splitList.append(data[x:x+3])
for backpack in splitList:
    commonCharOneTwo = ''.join(set(backpack[0]).intersection(backpack[1]))
    commonCharTwoThree = ''.join(set(backpack[1]).intersection(backpack[2]))
    commonChar = ''.join(set(commonCharOneTwo).intersection(commonCharTwoThree))
    solution.append(letterToNumber(commonChar.strip()))
print(sum(solution))