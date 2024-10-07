"""
baekjoon 13458 시험감독
"""
n = int(input())
hNum = list(map(int, input().split(' ')))
b, c = map(int, input().split(' '))

ttl = n
for h in hNum:
    if h > b:
        m = (h-b)//c
        na = (h-b)%c
        ttl += m
        if na > 0:
            ttl += 1
print(ttl)


'''
5
1 1 1 1 1
6 2
'''