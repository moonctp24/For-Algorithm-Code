"""
BAEKJOON 1931번 회의실 배정
https://www.acmicpc.net/problem/1931
"""

# 처음엔 젤 작은 시간순서로 정렬하고 순서대로 탐색하는 방식으로 풀었다. 
# 테스트케이스는 잘 돌아가는데, 제출하면 시간초과가 뜬다. 
# 구글링해보고 시간을 줄일 수 있는 방법 발견해서 수정해준다.

n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

# 사용 시간이 작은 순으로 정렬
for i in range(len(time)):
    min_time = 2147483647 # max of conference range
    min_index = len(time)
    for j in range(i, len(time)):
        if time[j][1]-time[j][0] < min_time:
            min_time = time[j][1]-time[j][0]
            min_index = j
    time[i], time[min_index] = time[min_index], time[i]

lastest_time = max(map(max, time))
earliest_time = min(map(min, time))

possible_time = []
for i in range(earliest_time, lastest_time+1):
    possible_time.append(0) # 0: possible, 1: impossible

state = False
count = 0
for s, e in time:
    cnt = 0
    for j in range(s, e):
        if possible_time[j] == 0:
            cnt += 1
    if cnt == e-s:
        state = True
    if state == True:
        for j in range(s, e):
            possible_time[j] = 1
        state = False
        count += 1

print(count)