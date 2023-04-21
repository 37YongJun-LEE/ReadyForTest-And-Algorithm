T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # K개 과제 제출한 사람
    submit = list(map(int, input().split()))
    submit_check = [0] * (N+1)

    for i in submit:
        submit_check[i] = 1

    print('#{}'.format(test_case), end = ' ')
    for i in range(1, N+1):
        if submit_check[i] == 0:
            print(i, end= ' ')
    print()






"""

2
5 3
2 5 3
7 2
4 6

"""