# 포인트 -- data[::-1]을 이용해서 역순으로 만드는 것을 기억해야
# 풀 수 있는 문제다. ssafy는 구글링을 허용하지 않으므로 반드시
# 암기해서 풀 것.
# 리스트의 역순 활용 문제

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    data = list()
    answer = 0
    n = int(input())

    for i in range(8):
        data.append(list(input()))

    # 가로탐색
    for i in range(8):
        for j in range(n, 9):
            row = data[i][j - n:j].copy()

            if row == row[::-1]:
                answer += 1

    # 세로탐색
    for i in range(8):
        for j in range(n, 9):
            col = []

            for k in range(1, n + 1):
                col.append(data[j - k][i])

            if col == col[::-1]:
                answer += 1

    print('#' + str(test_case), answer)

    # ///////////////////////////////////////////////////////////////////////////////////
