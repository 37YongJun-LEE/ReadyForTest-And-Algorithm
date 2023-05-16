############ 방법 2 : 대각선 합을 저장한 리스트 구현하기


N, M = map(int, input().split())
data = list( list(map(int, input().split())) for _ in range(N) )


left_sum = [0] * (200*200)
right_sum = [0] * (200*200)

for i in range(N):
    for j in range(M):
        left_sum[i + j] += data[i][j]
        right_sum[i - j + 200] += data[i][j]

answer = 0
for i in range(N):
    for j in range(M):
        answer = max( answer, left_sum[i+j] + right_sum[i-j+200] - data[i][j] )
print(answer)




"""
########## 방법 1

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

def check(x, y):
    sum = data[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while True:
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            sum += data[nx][ny]
            nx += dx[i]
            ny += dy[i]

    return sum


N, M = map(int, input().split())
data = list( list(map(int, input().split())) for _ in range(N) )
answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, check(i, j))
print(answer)

"""