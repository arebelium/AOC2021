from pyaoc import aoc

@aoc(2022, 9, 1)
def one(data=None):
    # data="R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"
    HrowI = 0
    HcolI = 0
    TrowI = 0
    TcolI = 0
    all={}
    all[str(TrowI)+":"+str(TcolI)] = 1
    for i in data.splitlines():
        for index in range(1, int(i.split(" ")[1])+1):
            match i.split(" ")[0]:
                case "R":
                    if HrowI==TrowI and HcolI==TcolI+1:
                        TcolI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI+1==TrowI and HcolI==TcolI+1:
                        TcolI+=1
                        TrowI-=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI==TrowI+1 and HcolI==TcolI+1:
                        TcolI+=1
                        TrowI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    HcolI+=1
                case "L":
                    if HrowI+1==TrowI and HcolI+1==TcolI:
                        TcolI-=1
                        TrowI-=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI==TrowI+1 and HcolI+1==TcolI:
                        TcolI-=1
                        TrowI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI==TrowI and HcolI+1==TcolI:
                        TcolI-=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    HcolI-=1
                case "U":
                    if HrowI==TrowI+1 and HcolI==TcolI+1:
                        TcolI+=1
                        TrowI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI==TrowI+1 and HcolI+1==TcolI:
                        TcolI-=1
                        TrowI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI==TrowI+1 and HcolI==TcolI:
                        TrowI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    HrowI+=1
                case "D":
                    if HrowI+1==TrowI and HcolI==TcolI:
                        TrowI-=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI+1==TrowI and HcolI==TcolI+1:
                        TrowI-=1
                        TcolI+=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    if HrowI+1==TrowI and HcolI+1==TcolI:
                        TrowI-=1
                        TcolI-=1
                        all[str(TrowI)+":"+str(TcolI)] = 1
                    HrowI-=1
    return(len(all))