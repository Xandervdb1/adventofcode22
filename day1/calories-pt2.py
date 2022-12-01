datafile = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day1\data.txt","r")
data = datafile.readlines()
sepList = []
tempElf = []
calories = []
topThree = []
for x in data:
    if x != "\n": #not a new tempElf
        if x.endswith("\n"): #check if not last value
            numberStr = x[:len(x)-1] #cut off "\n"
            number = int(numberStr) #change string to number
        else:
            number = int(x) #last value, so no cutting off
        tempElf.append(number) #use temp list to store current elf
    else: #encountered "\n" which means a new elf is next
        sepList.append(tempElf.copy()) #put current tempElf as a list inside the separated list
        tempElf.clear() #empty temp list
sepList.append(tempElf.copy()) #make sure to include last value since no "\n" will be next
for elf in sepList: #get the sum of calories for each list (elf) in separated list
    calories.append(sum(elf))
i = 1
while i < 4: #need to find top 3, so repeat 3 times
    topThree.append(max(calories)) #add biggest num to top 3 list
    calories.pop(calories.index(max(calories))) #remove biggest number from list
    i += 1
print(sum(topThree))