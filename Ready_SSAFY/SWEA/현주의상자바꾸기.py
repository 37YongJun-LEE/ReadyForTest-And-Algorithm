T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] + [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L,R+1):
            box[j] = i

    print('#{}'.format(test_case), end = ' ' )
    for k in range(1, N+1):
        print(box[k], end = ' ')
    print()
