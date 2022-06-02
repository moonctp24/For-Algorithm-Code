"""
BAEKJOON 12904번 A와 B
https://www.acmicpc.net/problem/12904
"""
def reverseStr(str):
    newStr = ''
    for i in str:
        if i == 'A':
            newStr += 'B'
        elif i == 'B':
            newStr += 'A'
    return newStr

def AmakeB(nowA, goalB):
    if nowA == goalB:
        return 1
    elif len(nowA) > len(goalB):
        return 0

    result1 = AmakeB(nowA + 'A', goalB)
    result2 = AmakeB(reverseStr(nowA) + 'B', goalB)
    
    if result1 == 0 and result2 == 0:
        return 0
    elif result1 == 1 or result2 == 1:
        return 1
    
A = input()
B = input()

result = AmakeB(A, B)

print(result)

'''
답은 옳게 나오는데, 시간초과 됨
'''