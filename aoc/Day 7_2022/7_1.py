from pyaoc import aoc
import re

@aoc(2022, 7, 1)
def one(data=None):
    all={}
    box=[]
    path=[]
    dirval={}
    data = data.splitlines()
    for i in range(1, len(data)):
        if data[i]=="$ ls":
            box = []
            while not data[i+1].startswith("$"):
                box.append(data[i+1])
                i+=1
                if i+1==len(data):
                    break
            all[''.join(path)] = box
        elif data[i].startswith("$ cd .."):
            path.pop()
        elif data[i].startswith("$ cd") and not data[i].startswith("$ cd .."):
            path.append(data[i].split(" ")[2])
    
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
    for i in dirval:
        if dirval[i]<=100000:
            summ+=dirval[i]   
    return(summ)   
    

     