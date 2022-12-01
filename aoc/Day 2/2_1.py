inputFile = open(r"C:\Users\justi\AOC2021\aoc2021\Day 2\2_input.txt", "r")
lines = inputFile.readlines()
horizontal = 0
depth = 0
for line in lines:
    if line.startswith("f"):
        horizontal += int(line.strip()[-1])
    elif line.startswith("u"):
        depth -= int(line.strip()[-1])
    elif line.startswith("d"):
        depth += int(line.strip()[-1])
print (horizontal*depth)
inputFile.close()
