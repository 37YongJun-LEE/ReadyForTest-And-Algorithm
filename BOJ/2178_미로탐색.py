from collections import deque

dx = [-1, +1, 0, 0] # 상하 좌 우
dy = [0, 0, -1, +1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if not visited[nx][ny] and data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                visited[nx][ny] = True
                queue.append([nx, ny])

N, M = map(int, input().split())
data = [ list(map(int, input())) for i in range(N)]
visited = [ [False] * M for i in range(N)]

bfs(0, 0)
print(data[N-1][M-1])

