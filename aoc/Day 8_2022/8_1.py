from pyaoc import aoc

@aoc(2022, 8, 1)
def one(data=None):
    # data = "121212011303121030310342042402\n021211021113201200034023433130\n112100131112221303204244242431\n020110213013113103013204332232\n253551324423543513123345241135\n201022331320201202140104411413\n154521232411313453434133354341\n515145541442431343352362313232"
    data = data.splitlines()
    count = 2*len(data)+2*len(data[0])-4
    max1C = [int(i[0]) for i in data][1:-1]
    maxLC = [int(i[-1]) for i in data][1:-1][::-1]
    max1L = [int(i) for i in data[0]][1:-1]
    maxLL = [int(i) for i in data[-1]][1:-1][::-1]
    data.pop(0)
    data.pop()
    data = [sub[1:-1] for sub in data]
    all = {}
    rowI = 0
    for row in data:
        colI = 0
        for col in row:
            if int(col)>max1C[rowI]:
                max1C[rowI] = int(col)
                all[str(rowI)+":"+str(colI)]="1"
            if int(col)>max1L[colI]:
                max1L[colI] = int(col)
                all[str(rowI)+":"+str(colI)]="1"
            colI+=1
        rowI+=1
    data = [row[::-1] for row in data[::-1]]
    rowI = 0
    for row in data:
        colI = 0
        for col in row:
            if int(col)>maxLC[rowI]:
                maxLC[rowI] = int(col)
                all[str(len(data)-rowI-1)+":"+str(len(row)-colI-1)]="1"
            if int(col)>maxLL[colI]:
                maxLL[colI] = int(col)
                all[str(len(data)-rowI-1)+":"+str(len(row)-colI-1)]="1"
            colI+=1
        rowI+=1
    count+=len(all)
    return(count)