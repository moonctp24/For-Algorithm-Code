'''
제약조건
1. 1 <= temperatures.length <= 10^5
2. 30 <= temperatures[i] <= 100
'''

# using stack
def hotterDay(temperatures):
    # answerList = []
    # for n in range(len(temperatures)):
    #     answerList.append(0)
    answerList = [0] * len(temperatures) # 위 세 줄을 한 줄로 간단화

    tStack = []
    for i in range(len(temperatures)):
        if(len(tStack)==0):
            tStack.append((temperatures[i],i))
        else:
            while tStack and tStack[-1][0] < temperatures[i]:
                lastT = tStack.pop()
                answerList[lastT[1]] = i-lastT[1]
            tStack.append((temperatures[i],i))
    return answerList

print(hotterDay([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0])
print(hotterDay([30,40,50,60]) == [1, 1, 1, 0])
print(hotterDay([30,60,90]) == [1, 1, 0])