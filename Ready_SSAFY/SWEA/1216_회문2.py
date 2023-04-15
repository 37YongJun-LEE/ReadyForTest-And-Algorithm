T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    tc = int(input())

    data = [list(input()) for _ in range(100)]

    max_answer = 2

    # 가로 탐색
    for i in range(100):  # 처음 가로줄부터
        for j in range(max_answer, 101):  # # j자리 회문부터 하나씩,
            for k in range(j, 101):  # 각 자리부터 j자리만큼

                # print(data[i][k-j:k])
                line = data[i][k - j:k].copy()
                if line == line[::-1]:
                    # print(len(line))
                    max_answer = max(max_answer, len(line))
                    # print(max_answer)
                    break  # 갱신하면, 중복계산 필요 없으므로 건너뛰기 위한 장치

    # 세로 탐색
    for i in range(100):  # 1번 세로줄 부터.. 마지막 줄까지.

        for line_digit in range(max_answer, 101):  # 1자리 회문일때, 2자리 회문일때,,... 마지막 100자리 회문 까지 확인

            for j in range(line_digit, 101):  # n자리 회문인 경우일때,
                col = []

                for k in range(1, line_digit + 1):  # n 자리 하나씩 넣기
                    col.append(data[j - k][i])

                if col == col[::-1]:
                    max_answer = max(max_answer, len(col))
                    # print(max_answer)
                    break
    print('#' + str(tc), max_answer)
    # ///////////////////////////////////////////////////////////////////////////////////
