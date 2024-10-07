"""
SWEA 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
"""

def findSameNum(num):
    sameNum = []
    tmpL = []
    for nn in num:
        if nn in tmpL: # find same num
            sameNum.append(nn)
        else: # find init num
            tmpL.append(nn)
    if len(sameNum) > 0:
        return True
    else:
        return False

n = int(input())
numList = [0 for _ in range(n)]
cntList = [0 for _ in range(n)]
for i in range(n):
    numList[i],cntList[i] = map(int, input().split(' '))

rstList = []
for i in range(n):
    nowList = list(str(numList[i]))
    maxI = len(nowList)-1
    minI = 0
    for c in range(10): # change count
        for a in range(len(nowList)-1,minI,-1): # find change point
            if nowList[a] > nowList[maxI]:
                maxI = a
        print(maxI, minI, nowList[maxI])
        nowMaxV = nowList[maxI]
        nowMinV = nowList[minI]
        if nowMaxV > nowMinV: # real change
            nowList[minI] = nowMaxV
            nowList[maxI] = nowMinV
        else:
            if not findSameNum(nowList):
                nowMaxV = nowList[-1]
                nowMinV = nowList[-2]
                nowList[-1] = nowMinV
                nowList[-2] = nowMaxV
        minI += 1
        c += 1
        
        if c == cntList[i]:
            break
        if minI == len(nowList):
            minI = 0
            if c%2 == 0:
                c = cntList[i]-1
            else:
                c = cntList[i]
            
    print(nowList)
    tmpStr = ''
    for c in range(len(nowList)):
        tmpStr += str(nowList[c])
    print(tmpStr)
    rstList.append(tmpStr)
    print(rstList)

for i in range(n):
    print('#'+str(i+1), rstList[i])

'''
4
123 1
2737 6
32888 2
94 3

#1 321
#2 7732
#3 88832
#4 49

1
543324 3
544323
'''