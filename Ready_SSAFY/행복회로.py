T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    answer = data[0]
    for i in range(1, N):
        if data[i] == 0 or data[i] == 1:
            answer += data[i]
        else:
            if answer == 0 or answer == 1:
                answer += data[i]
            else:
                answer *= data[i]
    #print('#{} {}'.format(test_case, answer))

