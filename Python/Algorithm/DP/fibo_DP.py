
# Top-down
def fiboDP(n):
    fibo_list = {}
    if n == 1 or n == 2:
        return 1
    if n not in fibo_list:
        fibo_list[n] = fiboDP(n-1) + fiboDP(n-2)
    return fibo_list[n]

print(fiboDP(7))

# Bottom-Up
def fiboLite(n):
    memo = {}
    for i in range(1,n+1):
        if (i == 1 or i ==2):
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fiboLite(7))