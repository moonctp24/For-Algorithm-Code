'''
Shinhan SCOOLCHECK 코딩챌린저
문제2. 시험감독
'''

from math import ceil


testRoomCnt = int(input()) # 시험장 개수
testManCnt = list(map(int, input().split(' '))) # 각 시험장의 시험 응시자 수
ttlSprvsr,subSprvsr = map(int, input().split(' '))

sprvsrCnt = 0 # 필요한 감독관 수

for i in testManCnt:
    # 총 감독관은 각 시험장 오직 1명, 감시할 수 있는 응시자 수는 B(ttlSprvsr) 명 이다.
    sprvsrCnt = sprvsrCnt + 1 # 시험장 마다 총감독관 한명 배치
    i = i - ttlSprvsr # 각 시험장의 감독해야 할 응시자 수 빼주기

    # ceil(남은 응시자 / 부감독관이 감독할 수 있는 응시자 수)
    sprvsrCnt = sprvsrCnt + ceil(i / subSprvsr)

print(sprvsrCnt)