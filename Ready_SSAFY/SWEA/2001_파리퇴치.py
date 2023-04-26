T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = [ list(map(int, input().split())) for i in range(N) ]
    answer = 0
    for i in range(M-1, N):
        for j in range(M-1, N):
            temp = 0
            # mxm칸 출력해보기
            for h in range(M-1, -1, -1):
                print(data[i-h][j-M+1:j+1])
                temp += sum(data[i-h][j-M+1:j+1])
            answer = max(answer, temp)
    print('#{} {}'.format(test_case, answer))


"""
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

1
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

"""