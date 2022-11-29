inputFile = open(r"C:\Users\justi\AOC2021\aoc2021\1_input.txt", "r")
firstLine = int(inputFile.readline().strip())
secondLine = int(inputFile.readline().strip())
thirdLine = int(inputFile.readline().strip())
box = firstLine + secondLine + thirdLine
count = 0
lines = inputFile.readlines()
for line in lines:
    firstLine = secondLine
    secondLine = thirdLine
    thirdLine = int(line.strip())
    if (firstLine+secondLine+thirdLine)>box:
        count += 1
    box=firstLine+secondLine+thirdLine
print(count)
inputFile.close()    
