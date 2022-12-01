data = open(r"C:\Users\xande\Dropbox\PC\Desktop\adventofcode22\day1\data.txt","r").readlines()
sepList = []
tempElf = []
calories = []
for x in data:
    if x != "\n": #not a new tempElf
        if x.endswith("\n"): #check if not last value
            number = int(x.strip()) #change string to number, cut off "\n"
        else:
            number = int(x) #last value, so no cutting off
        tempElf.append(number) #use temp list to store current elf
    else: #encountered "\n" which means a new elf is next
        sepList.append(tempElf.copy()) #put current tempElf as a list inside the separated list
        tempElf.clear() #empty temp list
sepList.append(tempElf.copy()) #make sure to include last value since no "\n" will be next
for elf in sepList: #get the sum of calories for each list (elf) in separated list
    calories.append(sum(elf))
print(max(calories)) #get the max amount of calories from calories list