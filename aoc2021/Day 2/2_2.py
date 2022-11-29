inputFile = open(r"C:\Users\justi\AOC2021\aoc2021\Day 2\2_input.txt", "r")
lines = inputFile.readlines()
horizontal = 0
depth = 0
aim = 0
for line in lines:
    x = int(line.strip()[-1])
    if line.startswith("f"):
        horizontal += x
        depth += aim*x 
    elif line.startswith("u"):
        aim -= x
    elif line.startswith("d"):
        aim += x
print (horizontal*depth)
inputFile.close()
