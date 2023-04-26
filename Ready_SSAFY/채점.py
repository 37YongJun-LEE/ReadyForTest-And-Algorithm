T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    max_score = 0
    min_score = N
    for i in range(N):  # N명의 학생 M개의 문제수
        #problem_data = list(map(int, input().split()))
        score = sum(map(int, input().split()))
        max_score = max(max_score, score)
        min_score = min(min_score, score)
    print('#{} {} {}'.format(test_case, min_score, max_score))
