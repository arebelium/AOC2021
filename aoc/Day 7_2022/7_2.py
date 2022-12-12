from pyaoc import aoc
import re

@aoc(2022, 7, 2)
def two(data=None):
    all={}
    box=[]
    path=[]
    dirval={}
    data = data.splitlines()
    for i in range(1, len(data)):
        if data[i].startswith("$ cd") and not data[i].startswith("$ cd .."):
            path.append(data[i].split(" ")[2])
        if data[i].startswith("$ cd .."):
            path.pop()
        if data[i]=="$ ls":
            it = 1
            box = []
            while not data[i+it].startswith("$"):
                box.append(data[i+it])
                it+=1
                if it+i==len(data):
                    break
            all[''.join(path)] = box
    
    while any(any('dir' in s for s in subList) for subList in all.values()):
        for i in all:
                if not any("dir" in stri for stri in all[i]):
                    dirval[i]=sum(list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), all[i])))
                for j in all[i]:
                    if "dir" in j:
                        try:
                            all[i][all[i].index(j)] = str(dirval[i+j.split(" ")[1]])
                        except:
                            continue
    summ=0
    if not any("dir" in stri for stri in all[i]):
                    dirval[i]=sum(list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), all[i])))
    for i in all:
        for j in all[i]:
            summ+=(int(j.split(" ")[0]))
        break
    res = summ
    for i in dirval:
        if 70000000-summ+dirval[i]>=30000000:
            if dirval[i]< res:
                res=dirval[i]
    return(res)   
    

     