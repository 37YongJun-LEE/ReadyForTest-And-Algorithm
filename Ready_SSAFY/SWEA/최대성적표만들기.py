T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    print('#{} {}'.format(test_case, sum(score[-K:])))

"""

2
3 1
100 90 80
3 2
100 90 80
"""