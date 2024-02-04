"""
현대 Softeer 문제 Level2. 금고털이

*** 시간초과를 잡기위해 두 가지 사용 ***
1. input = sys.stdin.readline
2. [list(map(int,input().split())) for _ in range(n)]
"""
import sys
input = sys.stdin.readline

w, n = map(int, input().split())
jList = [list(map(int,input().split())) for _ in range(n)] # 아래 반복문보다 이게 시간이 덜 걸린대
# for i in range(n):
#     jw, jm = map(int, input().split()) # 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있다.
#     # jw, jm = map(int, sys.stdin.readline().split()) # 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않는다.
#     jList.append((jw, jm))
jList.sort(key=lambda x: (x[1]), reverse=True)

ans = 0
for c in jList:
    if w <= 0:
        break
    if w <= c[0]:
        ans += w * c[1]
        break
    else:
        w -= c[0]
        ans += c[0] * c[1]
print(ans)

'''
tc1
100 2
90 1
70 2

tc2
500 2
700 2
90 1
1000

tc3
50 5
7 10
3 44
50 1
132 + 70 + 40 = 242

tc4
100 3
20 1
30 1
60 2
120 + 30 + 10 = 160
'''