"""
BAEKJOON 15649번 N과M(1)
https://www.acmicpc.net/problem/15649
"""

from itertools import permutations

n,m = map(int, input().split())

tmp = []
for i in range(1, n+1):
    tmp.append(i)

for i in permutations(tmp, m):
    print(' '.join(map(str, i)))
