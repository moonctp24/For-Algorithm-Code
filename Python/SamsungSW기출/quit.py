"""
삼성SW 역량테스트 기출1
퇴사
"""

def main():
    quitN = int(input())
    ccList= [list(map(int, input().split(' '))) for _ in range(quitN)]
    rst = [0 for _ in range(quitN+1)]
    for i in range(quitN-1, -1, -1):
        if ccList[i][0] > (quitN-i):
            rst[i] = rst[i+1]
        else:
            rst[i] = max(rst[i+1], rst[i+ccList[i][0]]+ccList[i][1])

    print(rst[0])

    # result = []
    # for i in range(len(result)):
    #     print('#{} {}'.format(i+1, result[i]))
main()

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''