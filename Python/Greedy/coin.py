"""
BAEKJOON 11047번 동전 0
https://www.acmicpc.net/problem/11047
"""

def main():
    n, k = map(int, input().split())

    coin = []
    for i in range(n):
        money = int(input())
        coin.append(money)

    count = 0
    for i in range(n-1, -1, -1):
        count += (k//coin[i])
        k %= int(coin[i])
    
    print(count)

if __name__=="__main__":
    main()