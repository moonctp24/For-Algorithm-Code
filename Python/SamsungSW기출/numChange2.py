"""
SWEA 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
"""
def changeNum(rstList, num, cnt):
    if cnt == 0:
        tn = int(''.join(num))
        if tn not in rstList:
            rstList.append(tn)
            return
    # print('called', rstList, num, cnt)
    # num2 = num.copy()
    for a in range(len(num)):
        for b in range(a+1, len(num)):
            num[a], num[b] = num[b], num[a]
            # cnt -= 1
            changeNum(rstList, num, cnt-1)
            num[a], num[b] = num[b], num[a]

n = int(input())
for i in range(n):
    num, cnt = map(str, input().split(' '))
    cnt = int(cnt)
    num = list(num)
    rstList = []
    changeNum(rstList, num, cnt)
    print(max(rstList))

# a =['5', '4', '3', '3', '2', '4'] 
# print(int(''.join(a)))
    

'''
4
123 1
2737 6
32888 2
94 3

#1 321
#2 7732
#3 88832
#4 49

1
543324 3
544332

123456 -> 15 * 10
'''