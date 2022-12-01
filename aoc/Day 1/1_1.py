inputFile = open(r"C:\Users\justi\AOC2021\aoc2021\Day 1\1_input.txt", "r")
lines = inputFile.readlines()
count = 0
box = 0
for line in lines:
    if int(line) > box:
        count += 1
    box = int(line)
print (count-1)
inputFile.close()