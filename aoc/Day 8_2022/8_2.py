from pyaoc import aoc

@aoc(2022, 8, 2)
def two(data=None): 
    # data = "121212011303121030310342042402\n021211021113201200034023433130\n112100131112221303204244242431\n020110213013113103013204332232\n253551324423543513123345241135\n201022331320201202140104411413\n154521232411313453434133354341\n515145541442431343352362313232"
    # data = "30373\n25512\n65332\n33549\n35390"
    data = data.splitlines()
    countLeft = [0] * len(data)
    countRight = [0] * len(data)
    countUp = [0] * len(data)
    countDown = [0] * len(data)
    for i in range(len(data)):
        countLeft[i] = [0] * len(data[0])
        countRight[i] = [0] * len(data[0])
        countUp[i] = [0] * len(data[0])
        countDown[i] = [0] * len(data[0])
    rowI = 0
    for row in data:
        colI = 0
        for col in row:
            for i in range(colI-1,-1,-1):
                countLeft[rowI][colI]+=1
                if(int(row[i])>=int(col)):
                    break
            for i in range(colI+1,len(data[0])):
                countRight[rowI][colI]+=1
                if(int(row[i])>=int(col)):
                    break
            for i in range(rowI-1,-1,-1):
                countUp[rowI][colI]+=1
                if(int(data[i][colI])>=int(col)):
                    break
            for i in range(rowI+1,len(data)):
                countDown[rowI][colI]+=1
                if(int(data[i][colI])>=int(col)):
                    break
            colI+=1
        rowI+=1
    maxx=0
    for i in range(0,len(countLeft)):
        for j in range(0,len(countLeft[i])):
            maxx=max(countLeft[i][j]*countRight[i][j]*countUp[i][j]*countDown[i][j], maxx)
    return(maxx)