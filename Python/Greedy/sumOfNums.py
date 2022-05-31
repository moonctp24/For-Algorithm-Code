"""
BAEKJOON 1789번 수들의 합
https://www.acmicpc.net/problem/1789
"""

numS = int(input())
remainingNumS = numS
count = 0
for i in range(1, numS+1):
    count += 1
    remainingNumS -= i
    if i+1 > remainingNumS:
        break

print(count)