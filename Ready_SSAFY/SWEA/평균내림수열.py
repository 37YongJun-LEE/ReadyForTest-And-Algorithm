T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_data = [0] + list(map(int, input().split()))
    Q = int(input())
    X = list(map(int, input().split()))

    a = [0] * (Q+1)
    print('#{}'.format(test_case), end=' ')
    for i in range(1, N+1): # a_i 초기값들 저장시키기
        a[i] = a_data[i]
        print(a[i], end = ' ')

    for idx in range(N+1, Q+1):
        a[idx] = sum(a[idx-N:idx]) // N
        print(a[idx], end = ' ')
    print()
"""
1
3
2 2 3
5
1 2 3 4 5
"""


"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_data = [0] + list(map(int, input().split()))
    Q = int(input())
    X = list(map(int, input().split()))

    a = [0] * (Q+1)

    for i in range(1, N+1): # a_i 초기값들 저장시키기
        a[i] = a_data[i]

    for idx in range(N+1, Q+1):
        #print(idx , a[idx])
        #for k in range(1, N+1):
        #    print(a[i-k], end = ' ')
        #print()

        a[idx] = sum( [a[idx-k] for k in range(1, N+1)] ) // N

    print(a)
    print('----------------------')

"""