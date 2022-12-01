from pyaoc import aoc

@aoc(2022, 1, 1)
def one(data=None):
   return max(sum(map(int, i.split('\n'))) for i in data.split('\n\n'))