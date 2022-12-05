from pyaoc import aoc
import re

@aoc(2022, 5, 1)
def one(data=None):
    total = []
    box = []
    for i in (list(data.split("\n\n")[0].splitlines())):
        box.append([i[1], i[5], i[9], i[13], i[17], i[21], i[25], i[29], i[33]])
    for i in zip(*box[::-1]):
        i = [value for value in i if value != " "]
        i.pop(0)
        total.append(i)
    answer = []
    for i in data.split("\n\n")[1].splitlines():
        listy = list(map(int,re.findall(r'\d+', i)))
        for j in range(0, listy[0]):
            total[listy[2]-1].append(total[listy[1]-1].pop())
    for z in total:
            answer.append(z.pop())
    return (''.join(answer))
    