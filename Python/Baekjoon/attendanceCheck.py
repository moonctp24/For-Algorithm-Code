import sys
n, k, q, m = map(int, sys.stdin.readline().split(' '))
kList = list(map(int, sys.stdin.readline().split(' ')))
qList = list(map(int, sys.stdin.readline().split(' ')))
mList = []
for i in range(m):
    s, e = map(int,sys.stdin.readline().split(' '))
    mList.append([s,e])
# print(mList)

q2List = []
for i in range(len(qList)):
    if qList[i] not in kList:
        q2List.append(qList[i])
# print(q2List)

nList = [0 for _ in range(n+3)]
nList[0], nList[1], nList[2] = 1, 1, 1
for i in range(3, n+3):
    for q in q2List:
        if i % q == 0:
            nList[i] = 1
            break

for i in range(len(kList)):
    nList[kList[i]] = 0
# print(nList)

# rst = 0
# for i in range(len(nList)):
#     if nList[i] == 0:
#         rst += 1
# print(rst)

# 시간초과
# for i in range(m):
#     s, e = mList[i][0], mList[i][1]
#     rst = 0
#     for j in range(s,e+1):
#         if nList[j] == 0:
#             rst += 1
#     print(rst)

# 누적합
attend = [0 for _ in range(n+3)]
attend[0], attend[1], attend[2] = 0, 0, 0
if nList[3] == 0:
    attend[3] = 1
for i in range(4, n+3):
    # print(i, nList[i])
    if nList[i] == 0:
        attend[i] = attend[i-1] +1
    else:
        attend[i] = attend[i-1]
for i in range(m):
    s, e = mList[i][0], mList[i][1]
    print(attend[e] - attend[s-1])

'''
1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)

2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과 Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.

4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)

10 1 3 1
7
3 5 7
3 12

3 4 5 6 7 8 9 10 11 12
        -
1   1 1 1   1 1     1

50 4 5 1
24 15 27 43
3 4 6 20 25
3 52

10 1 3 3
7
3 5 7
3 12
3 5
11 12

5 1 1 1
3
3
3 7
'''