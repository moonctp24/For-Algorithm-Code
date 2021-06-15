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

# 테케는 되는데 제출하면 시간초과 뜬다. 구글링 해보니 더 좋은 로직이 있길래 그걸로 구현해보자