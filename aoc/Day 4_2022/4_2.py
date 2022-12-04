from pyaoc import aoc
import re

@aoc(2022, 4, 2)
def two(data=None):  #fastest
  count = 0
  for i in data.splitlines():
    listy = list(map(int, re.findall(r'\d+', i)))
    if listy[0] <= listy[2] and listy[1] >= listy[2] or listy[0] >= listy[2] and listy[0] <= listy[3]:
      count += 1
  return count

# @aoc(2022, 4, 2)
# def two(data=None):  #readable
#   count = 0
#   for i in data.splitlines():
#     a, b, c, d = list(map(int, re.findall(r'\d+', i)))
#     if a <= c and b >= c or a >= c and a <= d:
#       count += 1
#   return count

# @aoc(2022, 4, 2) 
# def two(data=None): #faster (ish)
#     count = 0
#     for i in data.splitlines():
#         listy = list(map(int,re.findall(r'\d+', i)))
#         if listy[0]<=listy[2] and listy[1]>=listy[2]:
#             count+=1
#         elif listy[0]>=listy[2] and listy[0]<=listy[3]:
#             count+=1
#     return (count)

# @aoc(2022, 4, 2)
# def two(data=None):
#     count = 0
#     for i in data.splitlines():
#         listy = re.findall(r'\d+', i)
#         if not set(range(int(listy[0]),int(listy[1])+1)).isdisjoint(range(int(listy[2]),int(listy[3])+1)):
#             count+=1
#     return (count)

        