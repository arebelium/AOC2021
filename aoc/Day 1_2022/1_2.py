from pyaoc import aoc

@aoc(2022, 1, 2)
def two(data=None):
   listy = [sum(map(int, i.split('\n'))) for i in data.split('\n\n')]
   listy.sort()
   return (listy[-1]+listy[-2]+listy[-3])