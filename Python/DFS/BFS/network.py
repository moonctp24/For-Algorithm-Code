"""
https://programmers.co.kr/learn/courses/30/parts/12421
PROGRAMMERS DFS/BFS NETWORK
"""

visited = []

def dfs(index, computers):
    global visited
    
    visited[index] = 1
    for i in range(len(computers[index])):
        # 자기 자신이면 pass
        if i == index: continue
        if computers[index][i] == 1 and visited[i] != 1:
            dfs(i, computers)
    return 1

def solution(n, computers):
    global visited
    
    for i in range(n**2):
        visited.append(0)
    
    answer = 0
    for i in range(n):
        if visited[i] == 1: continue
        answer += dfs(i, computers)
    
    return answer

def main():
    n1 = 3
    n2 = 3
    n3 = 6

    computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    computers3 = [[1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1]]

    result1 = 2
    result2 = 1
    result3 = 3

    global visited
    visited.clear()
    if solution(n1, computers1) == result1: print("RIGHT1")
    visited.clear()
    if solution(n2, computers2) == result2: print("RIGHT2")
    visited.clear()
    if solution(n3, computers3) == result3: print("RIGHT3")

if __name__=="__main__":
    main()
