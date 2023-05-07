T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    sum = 0
    for i in range(N):
        if sum + 1 < data[i]: break
        sum += data[i]
    print(sum + 1)