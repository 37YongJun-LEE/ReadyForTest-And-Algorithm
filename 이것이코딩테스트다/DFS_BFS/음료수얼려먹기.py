
import sys
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# dfs로 풀거다.
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        # 상하좌우 탐색
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False


# 개수 출력
answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
