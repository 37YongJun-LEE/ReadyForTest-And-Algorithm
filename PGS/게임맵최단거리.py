from collections import deque
def bfs(x, y, maps, visited):
    dx = [1, 0, 0, -1]  # 하 우 좌 상
    dy = [0, 1, -1, 0]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        vx, vy = queue.popleft()  # x, y
        prev = maps[vx][vy]
        for i in range(4):
            vx = vx + dx[i]
            vy = vy + dy[i]
            if vx < 0 or vy < 0 or vx >= len(maps) or vy >= len(maps[0]):  # 범위 밖인지 판단
                vx = vx - dx[i]
                vy = vy - dy[i]  # 취소
                continue  # 건너뛰기
            if maps[vx][vy] == 0 or visited[vx][vy] == True:  # 범위 안이면 방문여부 판단
                vx = vx - dx[i]
                vy = vy - dy[i]  # 취소
                continue  # 건너뛰기
            queue.append((vx, vy))
            maps[vx][vy] = prev + maps[vx][vy]  # +1 # 이동 카운트 계산
            visited[vx][vy] = True  # 방문처리
            vx = vx - dx[i]
            vy = vy - dy[i]  # 다음 위해 원상복귀


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]

    bfs(0, 0, maps, visited)

    # 방문 여부 확인 코드

    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]

    return answer