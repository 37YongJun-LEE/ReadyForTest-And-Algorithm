T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    # 1<= i <= N

    if D == 0:
        print('#{} {}'.format(test_case, N))
        continue


    k = (N) // ((D*2) + 1)
    if (N) % ((D*2) + 1) == 0:
        print('#{} {}'.format(test_case, k))
    else:
        print('#{} {}'.format(test_case, k+1))



"""


3
5 1
5 2
100 3

"""