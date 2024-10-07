"""
SWEA 2072. 홀수만 더하기
"""

def main():
    n = int(input())
    for i in range(n):
        rst = 0
        tmp = list(map(int, input().split(' ')))
        for j in tmp:
            if j%2 == 1:
                rst += j

        # print result
        print('#'+str(i+1)+ ' '+ str(rst))
main()


'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
'''