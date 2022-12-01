datafile = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day1\data.txt","r")
data = datafile.readlines()

sepList = []
tempElf = []
calories = []

for x in data:
    if x != "\n": # not a new tempElf
        if x.endswith("\n"): #check if last value
            l = len(x) 
            numberStr = x[:l-1] #cut off "\n"
            number = int(numberStr) #change string to number
        else:
            number = int(x) #not last value, so no cutting off
        tempElf.append(number) #use temp list to store current elf
    else: #encountered "\n" which means a new elf is next
        copyOfElf = tempElf.copy() #copy because lists reference each other
        sepList.append(copyOfElf) #put current tempElf as a list inside the separated list
        tempElf.clear() #empty temp list
copyOfElf = tempElf.copy() #make sure to include last value since no "\n" will be next
sepList.append(copyOfElf)
tempElf.clear()
        
for elf in sepList: #get the sum of calories for each list (elf) in separated list
    calorie = sum(elf)
    calories.append(calorie)

max = max(calories) #get the max amount of calories from calories list
print(max)