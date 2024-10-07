"""
SWEA 1206. [S/W 문제해결 기본] 1일차 - View
"""
for t in range(10):
    n = int(input())
    buld = list(map(int, input().split(' ')))
    rst = 0
    for i in range(2, n-2):
        lView = min(buld[i]-buld[i-1], buld[i]-buld[i-2])
        rView = min(buld[i]-buld[i+1], buld[i]-buld[i+2])
        if(lView > 0 and rView > 0):
            rst += min(lView, rView)
    print('#'+str(t+1), rst)
'''
10
0 0 254 185 76 227 84 175 0 0
'''