from pyaoc import aoc
import re

@aoc(2022, 4, 1)
def one(data=None): #4x faster
    count = 0
    for i in data.splitlines():
        listy = list(map(int,re.findall(r'\d+', i)))
        if listy[0]<=listy[2] and listy[1]>=listy[3]:
            count+=1
        elif listy[0]>=listy[2] and listy[1]<=listy[3]:
            count+=1
    return (count)

# @aoc(2022, 4, 1)
# def one(data=None):
#     count = 0
#     for i in data.splitlines():
#         listy = re.findall(r'\d+', i)
#         if set(range(int(listy[0]),int(listy[1])+1)).issubset(range(int(listy[2]),int(listy[3])+1)) or set(range(int(listy[2]),int(listy[3])+1)).issubset(range(int(listy[0]),int(listy[1])+1)):
#             count+=1
#     return (count)