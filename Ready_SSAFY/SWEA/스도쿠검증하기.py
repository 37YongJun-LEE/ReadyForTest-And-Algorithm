T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = [ list(map(int, input().split())) for _ in range(9)]
    impossible = False
    for i in range(9): # i 행, 열을 전부 1~9 확인해보기
        row_check = [0] * 10
        col_check = [0] * 10
        xx_check = [1] * 9
        # 행 확인
        for j in range(9):
            row_check[data[i][j]] = 1
            col_check[data[j][i]] = 1

            if j % 2 == 0:
                xx_check = [0] * 10
                k = j
                for a in range(3):
                    for b in range(3):
                        xx_check[data[k-a][k-b]] = 1

        if sum(row_check) != 9 or sum(col_check) != 9 or sum(xx_check) != 9:
            impossible = True
            break

    if impossible:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, 1))


"""
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
"""


"""
# case 5
1
4 5 7 1 6 3 8 2 9
6 3 9 8 2 7 5 4 1
7 9 3 4 8 5 1 6 2
1 8 2 5 4 9 6 3 7
8 6 1 7 9 2 3 5 4
5 2 4 6 3 1 7 9 8
3 7 6 9 1 4 2 8 5
2 4 5 3 7 8 9 1 6
9 1 8 2 5 6 4 7 3


"""