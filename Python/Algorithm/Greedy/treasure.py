"""
BAEKJOON 1026번 보물
https://www.acmicpc.net/problem/1026
"""

N = int(input())
arryA = list(map(int, input().split(' ')))
arryB = list(map(int, input().split(' ')))

arryA.sort(reverse=True)
arryB.sort()

minSum = 0
for i in range(N):
    minSum += arryA[i] * arryB[i]

print(minSum)
'''
B를 오름차순으로 정렬
A를 내림차순으로 정렬
각자 곱하면서 더한 값 출력
'''