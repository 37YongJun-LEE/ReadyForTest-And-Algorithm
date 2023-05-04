N = int(input())

def dfs(row, visited):
    print(row)
    if row == N:
        return N
        exit()

    for col in range(N):
        if not visited[row][col]: continue

        visited[row][col] = False
        # 공격범위 처리
        # 가로 세로
        for i in range(N):
            visited[row][i] = False
            visited[i][col] = False

        # 대각선
        for i in range(N):
            #print(i, N)
            if 0 <= row - i < N and 0 <= col - i < N:
                visited[row-i][col-i] = False
            if 0 <= row + i < N and 0 <= col + i < N:
                visited[row+i][col+i] = False
            if 0 <= col - i < N and 0 <= row + i < N:
                visited[row+i][col-i] = False
            if 0 <= row - i < N and 0 <= col + i < N:
                visited[row-i][col+i] = False

        dfs(row+1, visited)
        # 공격범위 제거
        visited[row][col] = True

        # 가로 세로  공격범위 제거
        for i in range(N):
            visited[row][i] = True
            visited[i][col] = True

        # 대각선  공격범위 제거
        for i in range(N):
            #print(i, N)
            if 0 <= row - i < N and 0 <= col - i < N:
                visited[row - i][col - i] = True
            if 0 <= row + i < N and 0 <= col + i < N:
                visited[row + i][col + i] = True
            if 0 <= col - i < N and 0 <= row + i < N:
                visited[row + i][col - i] = True
            if 0 <= row - i < N and 0 <= col + i < N:
                visited[row - i][col + i] = True
        if row == N:
            return True
    return False


visited = [ [True] * N for _ in range(N)]

#dfs(row, visited)
if dfs(0, visited):
    print(N)
else:
    print(False)

for i in range(N):
    print(visited[i])