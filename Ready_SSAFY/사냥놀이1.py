from collections import deque

def bfs(x, y, data, visited):
    global tmp
    tmp += data[x][y]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    dx = [-1, +1, -1, +1]
    dy = [-1, +1, +1, -1]

    while queue:
        x1, y1 = queue.popleft()
        tmp += data[x1][y1]
        print(x1, y1)
        for i in range(4):
            if x1 + dx[i] < 0 or y1 + dy[i] < 0 or x1 + dx[i] >= N or y1 + dy[i] >= N:
                continue
            if not visited[x1 + dx[i]][y1 + dy[i]]:
                queue.append( [x1 + dx[i], y1 + dy[i]] )
                visited[x1 + dx[i]][y1 + dy[i]] = True





N, M = map(int, input().split())

data = list( list(map(int, input().split())) for _ in range(N) )

answer = 0
tmp = 0
visited = list( [False] * M for _ in range(N))


"""
for i in range(N):
    for j in range(M):
        tmp = 0
        dfs(i, j, data)
        answer = max(answer, tmp)
"""

bfs(3, 3, data, visited)

print(tmp)

for i in range(N):
    print(visited[i])
