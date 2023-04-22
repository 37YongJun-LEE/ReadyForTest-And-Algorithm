T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    # print(L, U, X)
    if L <= X <= U:
        print('#{} {}'.format(test_case, 0))
    else:
        if X < L:
            print('#{} {}'.format(test_case, L - X))
        elif X > U:
            print('#{} {}'.format(test_case, -1))

