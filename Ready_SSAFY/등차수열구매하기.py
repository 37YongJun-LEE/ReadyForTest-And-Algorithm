T = int(input())
for test_case in range(1, T+1):
    N, X, E = map(int, input().split())
    product = list(map(int, input().split()))
    cnt = 0
    target_range = [ i for i in range(X-E, X+E+1) ]
    for i in product:
        if i > target_range[-1]: # 범위보다 첫항이 큰수는 계산 필요 x
            continue
        for j in target_range: # i 가 j 보다 작은 경우는 반대로 계산해서 나누어 떨어지는지 봐야한다.
            if i < j:
                if j % i == 0:
                    cnt += 1
                    break
            else:
                if i % j == 0:
                    cnt += 1
                    break
    print('#{} {}'.format(test_case, cnt))




"""
T = int(input())
for test_case in range(1, T+1):
    N, X, E = map(int, input().split())
    product = list(map(int, input().split()))
    
    print('지금 범위 :', end = '')
    for i in range(X-E, X+E+1):
        print(i, end = ' ')
    print()

    cnt = 0
    target_range = [ i for i in range(X-E, X+E+1) ]
    for i in product:
        if i > target_range[-1]: # 범위보다 첫항이 큰수는 계산 필요 x
            continue
        for j in target_range:
            # i 가 j 보다 작은 경우는 반대로 계산해서 나누어 떨어지는지 봐야한다.
            if i < j:
                if j % i == 0:
                    print(j , end = ' ')
                    cnt += 1
                    break
            else:
                if i % j == 0:
                    print(j, end = ' ')
                    cnt += 1
                    break
    print()
    print('#{} {}'.format(test_case, cnt))


"""