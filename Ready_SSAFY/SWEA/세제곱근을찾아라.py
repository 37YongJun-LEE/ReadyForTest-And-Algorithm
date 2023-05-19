T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    flag = True
    for i in range(1, N + 1):
        if i ** (3) > N:
            flag = False
            break

        if i ** (3) == N:
            print('#{} {}'.format(test_case, i))
            flag = True
            break

    if not flag:
        print('#{} {}'.format(test_case, -1))