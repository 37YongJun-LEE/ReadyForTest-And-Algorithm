T = int(input())
for test_case in range(1, T+1):
    N, S = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    L, R = data[0], data[-1]
    answer = 0
    if abs(L - S) > abs(R - S):
        answer = abs(R-S) + R-L
    else:
        answer = abs(L-S) + R-L
    print(answer)
