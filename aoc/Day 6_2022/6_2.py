from pyaoc import aoc

@aoc(2022, 6, 2)
def two(data=None):
    for i in range(14, len(data)):
        if len(set(data[i:i+14:1])) == 14:
            return(i+14)