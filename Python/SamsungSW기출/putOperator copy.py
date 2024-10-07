"""
baekjoon 14888 연산자 끼워넣기
"""
from itertools import permutations

def plus(a, b):
    return a+b
def minus(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if a < 0 and b >= 0:
        return -(((-1)*a)//b)
    elif a >= 0 and b < 0:
        # return -(a//((-1)*b))
        return a//b
    elif a < 0 and b < 0:
        a = -1*a
        b = -1*b
        return a//b
    else:
        return a//b

n = int(input())
numL = list(map(int, input().split(' ')))
oprt = {'+':0, '-':0, 'x':0, '/':0}
oprtL = []
oprtNL = list(map(int, input().split(' ')))
for i in range(4):
    for j in range(oprtNL[i]):
        if i == 0:
            oprtL.append('+')
        elif i == 1:
            oprtL.append('-')
        elif i == 2:
            oprtL.append('x')
        else:
            oprtL.append('/')
oprtSet = list(permutations(oprtL)) # 연산자조합 생성
oprtSet = list(set(oprtSet)) # 중복제거

maxV, minV = 0, 0
for s in oprtSet:
    # print(s)
    nowV = numL[0]
    for i in range(n-1):
        # print(s[i], nowV)
        if s[i] == '+':
            nowV = plus(nowV, numL[i+1])
        elif s[i] == '-':
            nowV = minus(nowV, numL[i+1])
        elif s[i] == 'x':
            nowV = multi(nowV, numL[i+1])
        else:
            nowV = int(div(nowV, numL[i+1]))
    if maxV < nowV or maxV == 0:
        maxV = nowV
    if minV > nowV or minV == 0:
        minV = nowV
    # print('max:', maxV, '/ min:',minV)
print(maxV)
print(minV)
'''
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1

3
1 100 2
0 1 0 1

2
-9 3
0 0 0 1

4
1 1 1 1
0 1 2 0

5x6

3+4x5 = 35
3x4+5 = 17

1-100/2 = -49
1/100-2 = -2
'''