from pyaoc import aoc

@aoc(2022, 2, 1)
def one(data=None):
    points = {
        "AX": 4, "AY": 8, "AZ": 3,
        "BX": 1, "BY": 5, "BZ": 9,
        "CX": 7, "CY": 2, "CZ": 6
    }
    return (sum(points[i] for i in list(data.replace(" ", "").splitlines())))
