'''
Shinhan SCOOLCHECK 코딩챌린저
문제3. 셀프 넘버
'''

# 1 ~ 10000 까지의 모든 생성자 만들기
rangeNum = set(range(1, 10001))


# 생성자로서의 수열 만들기
notSelfNumList = set()
for i in rangeNum:
    tmp = i
    for j in str(i):
        tmp = tmp + int(j)
    notSelfNumList.add(tmp)

selfNumList = sorted(rangeNum - notSelfNumList)

for i in selfNumList:
    print(i)