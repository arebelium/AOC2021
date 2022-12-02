from pyaoc import aoc

@aoc(2022, 2, 2)
def one(data=None):
    points = {
        "AX": 3, "AY": 4, "AZ": 8,
        "BX": 1, "BY": 5, "BZ": 9,
        "CX": 2, "CY": 6, "CZ": 7
    }
    return (sum(points[i] for i in list(data.replace(" ", "").splitlines())))