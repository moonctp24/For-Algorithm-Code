"""
BAEKJOON 1439번 뒤집기
https://www.acmicpc.net/problem/1439
"""
str = input()
count0 = 0
count1 = 0

preNum = str[0]
if preNum == '0':
    count0 += 1
elif preNum == '1':
    count1 += 1

for i in str:
    if preNum == '1' and i == '0':
        count0 += 1
        preNum = '0'
    elif preNum == '0' and i == '1':
        count1 += 1
        preNum = '1'

print(min(count0, count1))
'''
1. 0인 구간 count
2. 1인 구간 count
3. 더 작은 거 출력
'''