def solution(m, n, puddles):
    answer = 0

    dp = []  # 2차원 배열 dp 초기화
    for i in range(n):
        dp.append([0 for _ in range(m)])

    dp[0][0] = 1  # 집 위치 시작 1
    for p in puddles:  # 물 울덩이 -1로 예외처리
        a, b = p
        dp[b - 1][a - 1] = -1

    for i in range(n):  # up 과 left 값을 더해야한다
        for j in range(m):
            if i == 0 and j == 0:
                continue

            if dp[i][j] < 0:
                continue

            if j == 0:  # 맨앞 줄은 left = 0 , 그리고 물웅덩이 -1 계산 없애기
                left = 0
            else:
                left = dp[i][j - 1]

            if i == 0:  # 범위 벗어나면 안되니 맨윗줄은 up = 0
                up = 0
            else:
                up = dp[i - 1][j]

            if left < 0:
                left = 0
            if up < 0:
                up = 0
            dp[i][j] = left + up

    print(dp)
    return dp[n - 1][m - 1] % 1000000007