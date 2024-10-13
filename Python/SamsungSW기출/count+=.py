t = int(input())
for tt in range(t):
    a, b, n = map(int, input().split(' '))
    cnt = 0
    while(a <= n and b <= n):
        if a > b:
            b += a
        else:
            a += b
        cnt += 1
    print(cnt)


'''
5
1 2 2
1 2 3
1 2 4
1 2 5
10 7 1293
'''