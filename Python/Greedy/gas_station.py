"""
BAEKJOON 13305번 주유소
https://www.acmicpc.net/problem/13305
"""

# comparision string value as int type
def comparison(a, b):
    if len(a) > len(b):
        return b
    elif len(a) < len(b):
        return a
    else : # len(a) == len(b)
        if a > b:
            return b
        elif a < b:
            return a
        else: # a = b:
            return a

n = int(input())
len_city = list(map(str, input().split(' ')))
gas = list(map(str, input().split(' ')))

max_index = len(len_city)
sum = 0
terminal = 0
for a in range(len(gas)):
    # terminal condition
    # if terminal == len(gas)-1: break

    min_value = '1000000000'
    for i in range(max_index): # -1 함
        min_value = comparison(min_value, gas[i])
    min_index = gas.index(min_value)

    for i in range(min_index, max_index):
        sum += int(len_city[i])*int(min_value)
        a += 1 # +1 when visit each city
    
    max_index = min_index

print(sum, terminal)

'''
도시 N(2 ≤ N ≤ 100,000)
도시까지의 거리는 1이상 1,000,000,000 이하의 자연수
리터당 가격은 1 이상 1,000,000,000 이하의 자연수
10억을 어예계산하냐 -> string으로 바꿔야하나?
1. 가장 기름 값이 싼 곳에서 그 뒤에까지 주유
2. 그 전까지 다음으로 가장 기름이 싼 곳에서 주유
~~

'''