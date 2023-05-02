## template
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    reserve = list(map(int, input().split()))
    reserve.sort()
    sum = 0
    for i in range(N):
        #print(i+1, reserve[i])
        sum += abs(i+1 - reserve[i])
    print('#{} {}'.format(test_case, sum))
