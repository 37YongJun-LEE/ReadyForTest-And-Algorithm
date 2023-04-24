"""T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N, M
    data = [ list(input()) for i in range(N) ]

    # 1, -1, 0 으로 바꾸는 코드
    for i in range(N):
        for j in range(M):
            if data[i][j] == "#":
                data[i][j] = 1
            if data[i][j] == ".":
                data[i][j] = -1

            if data[i][j] == "?":
                data[i][j] = 0


    # 바꿔진 코드를 인접 2개 곱이 -1의 여부로 판단
    # 첫번째만 바꾸기

    for i in range(1, M+1):
        F, B = data[0][i-1], data[0][i]

        if F == 0 or B == 0:




        #else:


    print('--------------------------')


"""


"""

3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.

"""