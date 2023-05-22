from collections import deque
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N = int(input())
k = int(input())
graph = list( list() for i in range(N+1))
for i in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
visited[0] = True

bfs(1)
cnt= 0
for i in range(1, N+1):
    if visited[i]:
        cnt += 1
print(cnt-1)