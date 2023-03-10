import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, start = map(int, input().split())
visited = [False]*(n+1)
graph = [ [] for i in range(n+1) ]  # 0번 인덱스는 없음 (0번노드는 없으므로)

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in graph:
    j.sort()

#print('dfs')
dfs(graph, start, visited)
print()
visited = [False]*(n+1)
bfs(graph, start, visited)
