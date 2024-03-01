from collections import deque

graph = {}
def graphBFS(graph, start_v):
    visited = [start_v]
    q = deque(start_v)
    while q:
        cur_node = q.popleft()
        for v in graph[cur_node]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited