"""
BAEKJOON 16953번 A -> B
https://www.acmicpc.net/problem/16953
"""
def makeCnt(nowCnt, nowA, goalB):
    # print(nowCnt, nowA, goalB)
    if nowA == goalB:
        return nowCnt
    elif int(nowA) > int(goalB):
        return -1

    nowCnt += 1
    result1 = makeCnt(nowCnt, str(int(nowA) * 2), goalB)
    result2 = makeCnt(nowCnt, nowA + '1', goalB)
    
    if result1 == -1 and result2 == -1:
        return -1
    elif result1 != -1 and result2 != -1:
        return min(result1, result2)
    else:
        return max(result1, result2)
    
A, B = map(str, input().split(' '))

result = makeCnt(1, A, B)

print(result)