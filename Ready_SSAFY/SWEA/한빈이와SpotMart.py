# 파이썬 풀이
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if a[i] + a[j] <= M:
                answer = max(answer, a[i] + a[j])

    if answer == 0:
        print(-1)
    else:
        print(answer)


"""

4
3 45
20 20 20
6 10
1 2 5 8 9 11
4 100
80 80 60 60
4 20
10 5 10 16
"""

