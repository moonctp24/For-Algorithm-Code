n, k = map(int, input().split(' '))
wL = [0]
vL = [0]
for i in range(n):
    w,v = map(int, input().split(' '))
    wL.append(w)
    vL.append(v)
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if wL[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wL[i]]+vL[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])