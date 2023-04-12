T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    tc = int(input())

    data = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    # 행의 최댓값
    for i in range(100):
        answer = max(answer, sum(data[i]))

    # 열의 최댓값
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += data[j][i]

        answer = max(answer, col_sum)

    # 대각선 최댓값
    cross_sum = 0
    xcross_sum = 0
    for i in range(100):
        cross_sum += data[i][i]

        xcross_sum += data[99 - i][i]

        answer = max(answer, cross_sum, xcross_sum)

    print('#' + str(tc), answer)

