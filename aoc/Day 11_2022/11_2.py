from pyaoc import aoc
import re

@aoc(2022, 11, 2)
def two(data=None):
    listy = []
    divideBy = []
    inspect = []
    # data="Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1"
    for i in data.split("\n\n"):
        listy.append(list(map(int,re.findall(r'\d+', i.splitlines()[1]))))
        divideBy.append(int(i.splitlines()[3].split(" ")[-1]))
        inspect.append(0)
    for i in range(0,10000):
        # print(i)
        for all in listy[0]:
            inspect[0]+=1
            newAll=all*7%9699690
            # print(newAll,divideBy[0],newAll%divideBy[0]==0)
            if(newAll%divideBy[0]==0):
                listy[6].append(newAll)
            else:
                listy[7].append(newAll)
        listy[0]=[]
        for all in listy[1]:
            inspect[1]+=1
            newAll=(all*11)%9699690
            if(newAll%divideBy[1]==0):
                listy[3].append(newAll)
            else:
                listy[5].append(newAll)
        listy[1]=[]
        for all in listy[2]:
            inspect[2]+=1
            newAll=(all+8)%9699690
            if(newAll%divideBy[2]==0):
                listy[0].append(newAll)
            else:
                listy[6].append(newAll)
        listy[2]=[]
        for all in listy[3]:
            inspect[3]+=1
            newAll=(all+7)%9699690
            if(newAll%divideBy[3]==0):
                listy[2].append(newAll)
            else:
                listy[4].append(newAll)
        listy[3]=[]
        for all in listy[4]:
            inspect[4]+=1
            newAll=(all+5)%9699690
            if(newAll%divideBy[4]==0):
                listy[2].append(newAll)
            else:
                listy[0].append(newAll)
        listy[4]=[]
        for all in listy[5]:
            inspect[5]+=1
            newAll=(all+4)%9699690
            if(newAll%divideBy[5]==0):
                listy[4].append(newAll)
            else:
                listy[3].append(newAll)
        listy[5]=[]
        for all in listy[6]:
            inspect[6]+=1
            newAll=(all*all)%9699690
            if(newAll%divideBy[6]==0):
                listy[7].append(newAll)
            else:
                listy[1].append(newAll)
        listy[6]=[]
        for all in listy[7]:
            inspect[7]+=1
            newAll=(all+3)%9699690
            if(newAll%divideBy[7]==0):
                listy[5].append(newAll)
            else:
                listy[1].append(newAll)
        listy[7]=[]
    result = max(inspect)
    inspect.remove(result)
    return(result*max(inspect))