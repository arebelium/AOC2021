from pyaoc import aoc

@aoc(2022, 3, 1)
def one(data=None):
    value = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53)))
    return sum(value[list(set(i[:len(i)//2]).intersection(i[len(i)//2:]))[0]] for i in list(data.splitlines()))