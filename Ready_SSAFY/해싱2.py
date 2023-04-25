T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = -100000000000

    for i in range(N-M+1): # N-M 만큼 할것.
        temp = 0
        for a, b in zip(A[i:M+i], B[0:M]):
            #print(a, b)
            temp += a*b
            #print(temp, end = ' ')
        answer = max(answer, temp)

    print('#{} {}'.format(test_case, answer))
