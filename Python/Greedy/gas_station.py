"""
BAEKJOON 13305번 주유소
https://www.acmicpc.net/problem/13305
"""
# 더 쉬운 로직으로 개선
# 처음 기름 값으로 계속 계산하면서 더 낮은 기름값이 나오면 그걸로 계산 반복

n = int(input())
len_city = list(map(int, input().split(' ')))
gas = list(map(int, input().split(' ')))

sum = 0
min_val = gas[0]
for i in range(len(gas)-1):
    if gas[i] < min_val:
        min_val = gas[i]
    sum += min_val*len_city[i]

print(sum)