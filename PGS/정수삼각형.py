def solution(triangle):
    answer = 0

    dp_table = [[0] * (2 ** h) for h in range(len(triangle))]  # dp 테이블 초기화
    dp_table[0] = [triangle[0][0]]  # 0번지 설정

    for i in range(1, len(dp_table)):
        k = 0
        for j in range(len(dp_table[i])):
            if j % 2 == 1:
                k += 1
            print(dp_table[i])
            print('j값: ', j, 'k값', k)

            try:
                dp_table[i][j] = dp_table[i - 1][j - k] + triangle[i][k]
            except:
                continue

    print(dp_table)
    return answer