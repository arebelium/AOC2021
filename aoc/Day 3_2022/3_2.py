from pyaoc import aoc
import re

@aoc(2022, 3, 2)
def two(data=None):
    value = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53)))
    listy = re.findall('((?:[^\n]+\n?){1,3})', data) #sadala pa 3 rindām
    return sum(value[list(set(i.splitlines()[0]).intersection(i.splitlines()[1]).intersection(i.splitlines()[2]))[0]] for i in listy)
