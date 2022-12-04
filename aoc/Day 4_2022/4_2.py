from pyaoc import aoc
import re

@aoc(2022, 4, 2) 
def two(data=None): #faster
    count = 0
    for i in data.splitlines():
        listy = re.findall(r'\d+', i)
        if int(listy[0])<=int(listy[2]) and int(listy[1])>=int(listy[2]):
            count+=1
        elif int(listy[0])>=int(listy[2]) and int(listy[0])<=int(listy[3]):
            count+=1
    return (count)

# @aoc(2022, 4, 2)
# def two(data=None):
#     count = 0
#     for i in data.splitlines():
#         listy = re.findall(r'\d+', i)
#         if not set(range(int(listy[0]),int(listy[1])+1)).isdisjoint(range(int(listy[2]),int(listy[3])+1)):
#             count+=1
#     return (count)

        