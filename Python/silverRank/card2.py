# 1. N의 값 입력
n = int(input())

# 2. 1부터 N까지의 리스트 만들기
nList = []
for i in range(n):
    nList.append(i+1)

print(nList)

# 제일 위에 있는 카드를 한장 버리는 함수
def dropTopNum(aList):
    print(1)


# 2. 제일 위 카드를 제일 밑 카드 밑으로 보낸다.

'''
예) 6
123456
1. 23456
2. 34562

1. 4562
2. 5624

1. 624
2. 246

1. 46
2. 64

1. 4
result = 4
'''