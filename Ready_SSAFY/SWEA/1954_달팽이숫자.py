# 다시 풀어보기... 꼭 다시 풀기 기본중에 기본
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    snail = [[0] * (N) for i in range(N)]
    row = 0
    col = 0
    dist = 0    # 우, 하, 좌, 상

    for n in range(1, N*N+1): # N*N번 실행해야한다.
        snail[row][col] = n
        row += drow[dist]
        col += dcol[dist]

        if row < 0 or col < 0 or row >= N or col >= N or snail[row][col] != 0:
            row -= drow[dist]
            col -= dcol[dist]
            dist = (dist + 1) % 4

            row += drow[dist]
            col += dcol[dist]

    print('#{}'.format(test_case))
    for i in snail:
        print(*i)
    print()

"""
# 적용 확인 코드
for i in range(N):
    print(snail[i])
"""



