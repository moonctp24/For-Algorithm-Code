'''
Number of Islands
'''
from collections import deque

def graphTravel(grph):
    count = 0
    
    m = len(grph)
    n = len(grph[0])
    checked = [[False]*n for _ in range(m)]
    
    def bfs(x,y):
        checked[x][y] = True
        q = deque()
        q.append((x,y))
        while q:
            cur_x, cur_y = q.popleft()
            
            # 암시적 그래프의 상하좌우 움직임 계산
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                # 없는 좌표 방문x & 값이 0인 곳 방문x & 방문했던 곳 방문x
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grph[next_x][next_y] == '1' and not checked[next_x][next_y]:
                        checked[next_x][next_y] = True
                        q.append((next_x, next_y))
        print(checked)
        return 1
        
    for i in range(m):
        for j in range(n):
            if grph[i][j] == '1' and not checked[i][j]:
                # print(grph[i][j])
                bfs(i, j)
                count += 1
    return count

print(graphTravel([
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
]) == 1)

print(graphTravel([
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1'],
]) == 3)