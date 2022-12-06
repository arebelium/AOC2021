from pyaoc import aoc

@aoc(2022, 6, 1)
def one(data=None):
    for i in range(4, len(data)):
        if len(set(data[i:i+4:1])) == 4:
            return(i+4)