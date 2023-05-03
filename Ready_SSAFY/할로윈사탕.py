T = int(input())
for test_case in range(1, T + 1):
    cnt = 0  # 몇번째 년도
    N = int(input())
    want = list(map(int, input().split()))

    while True:
        want2 = want.copy()
        cnt += 1






"""
T = int(input())
for test_case in range(1, T + 1):
    cnt = 0  # 몇번째 년도
    N = int(input())
    want = list(map(int, input().split()))
    total_candy = 0
    while True:
        want2 = want.copy()
        total_candy += N
        cnt += 1
        if total_candy < sum(want):
            break
        total_candy -= sum(want)

        # 내년 원하는 캔디수 갱신 코드
        for i in range(6):
            if i % 2 == 0:
                want[i] += want2[1] + want2[3] + want2[5]
            else:
                want[i] += want2[0] + want2[2] + want2[4]

    print('#{} {}'.format(test_case, cnt))

"""