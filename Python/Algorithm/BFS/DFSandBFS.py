"""
BAEKJOON 1269번 DFS와 BFS
https://www.acmicpc.net/problem/1260
"""
# 간단 알고리즘 짰음

n = int(input())
m = int(input())
v = int(input())

# graph = map(list(input()))

answer = []
visited = []

# 첫 방문 노드 v
answer.append(v)
visited[v] = 1

def dfs(v, graph):
    # terminal condition
    if 0 in visited:
        v = update next node
        visited[v] = 1
        answer.append(v)
        dfs(v, graph)
    else:
        break

dfs(v, graph)

print(answer)