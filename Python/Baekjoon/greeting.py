n = int(input())
if n == 0:
    print(0)
else:
    strong = list(map(int, input().split(' ')))
    pls = list(map(int, input().split(' ')))
    L = [0] + strong
    J = [0] + pls
    # print(L, J)
    dp = [[0 for _ in range(101)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, 101):
            if L[i] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][99])
'''
3
1 21 79
20 30 25

5
1 0 0 10 1
100 20 0 0 10

0  1   1  10 0
20 100 10 0  0
130

4
98 1 1 1
10 200 10 1
211

2
1 99
2 99

10
99 1 1 1 1 1 1 1 1 1
120 20 20 20 20 20 20 20 20 1
161
'''