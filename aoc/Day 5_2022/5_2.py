from pyaoc import aoc
import re

@aoc(2022, 5, 1)
def one(data=None):
    total = []
    answer = []
    total.append(['D', 'L', 'V', 'T', 'M', 'H', 'F'])
    total.append(['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P'])
    total.append(['R', 'S', 'D', 'M', 'P', 'H'])
    total.append(['L', 'B', 'V', 'F'])
    total.append(['N', 'H', 'G', 'L', 'Q'])
    total.append(['W', 'B', 'D', 'G', 'R', 'M', 'P'])
    total.append(['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q'])
    total.append(['C', 'L', 'W'])
    total.append(['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T'])
    for i in data.split("\n\n")[1].splitlines():
        box = []
        listy = list(map(int,re.findall(r'\d+', i)))
        for j in range(0, listy[0]):
            box.append(total[listy[1]-1].pop())
        for j in range(0, listy[0]):
            total[listy[2]-1].append(box.pop())
    for z in total:
            answer.append(z.pop())
    return (''.join(answer))
    