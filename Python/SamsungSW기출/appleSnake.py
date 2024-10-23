from collections import deque

# def print2list(li):
#     for i in range(len(li)):
#         print(li[i])

N = int(input())
K = int(input())
applePos = []
for i in range(K):
    a,b = map(int, input().split(' '))
    applePos.append([a, b]) # a-1 b-1?
# print(applePos)
direcChngN = int(input())
# direcChngL = []
direcChngD = {}
for i in range(direcChngN):
    a, b = map(str, input().split(' '))
    # direcChngL.append([int(a), b])
    direcChngD[int(a)+1] = b
# print(direcChngD)

mapL = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i == 0 or j == 0:
            mapL[i][j] = 1
        else:
            mapL[i][j] = 0
# print2list(mapL)

x, y = 1, 1
initH = [x, y] # init head
# initT = [x, y] # init tail
snkTrc = deque()
snkTrc.append(initH)
# print(snkTrc)
mapL[x][y] = 1
# print2list(mapL)
nowDirec = 'R' # R, L, U, D
tim = 0 # time
while(True):
    tim += 1
    if tim in direcChngD:
        # print('direction change')
        if direcChngD[tim] == 'L':
            if nowDirec == 'R':
                nowDirec = 'U'
            elif nowDirec == 'L':
                nowDirec = 'D'
            elif nowDirec == 'U':
                nowDirec = 'L'
            elif nowDirec == 'D':
                nowDirec = 'R'
        elif direcChngD[tim] == 'D':
            if nowDirec == 'R':
                nowDirec = 'D'
            elif nowDirec == 'L':
                nowDirec = 'U'
            elif nowDirec == 'U':
                nowDirec = 'R'
            elif nowDirec == 'D':
                nowDirec = 'L'
    # print('nowDirec:',nowDirec)
    if nowDirec == 'R':
        y += 1
    elif nowDirec == 'L':
        y -=1
    elif nowDirec == 'U':
        x -=1
    elif nowDirec == 'D':
        x += 1
    # print(x, y)   
    if x >= N+1 or y >= N+1: # game over2
        break 
    if mapL[x][y] != 0: # game over
        break
    
    # head move
    initH = [x, y]
    mapL[initH[0]][initH[1]] = 1
    snkTrc.append([x, y])
    
    if [x, y] in applePos: # 사과 포지션 도착
        # tail no move
        applePos.remove([x, y])
        # print('meet apple')
    else:
        txy = snkTrc.popleft()
        mapL[txy[0]][txy[1]] = 0
        # tail move
    # print2list(mapL)
print(tim)
            

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

L: left
D: right

1,1 1,2 1,3
2,1 2,2 2,3
3,1 3,2 3,3
'''