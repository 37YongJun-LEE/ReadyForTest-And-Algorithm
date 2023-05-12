T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 1번 팀원부터 시작이므로 인덱스 떄문에 0 추가 ( 0~N 까지 존재 )
    # 현재값
    score = [0] + list(map(int, input().split()))
    total_sum = sum(score)
    # 목표값
    target = [ max(score[i] + i , i) for i in range(N+1)]
    data = [ b - a for a, b in zip(score, target) ]  # 증가폭 데이터
    data.sort(reverse = True)

    cnt = 0
    for i in data:
        if total_sum >= 2 * N: break
        total_sum += i
        cnt += 1
    print('#{} {}'.format(test_case, cnt))



"""
# 1 번
T = int(input())
for test_case in range(1, T+1):
    N, S = map(int, input().split())
    resque = list(map(int, input().split()))
    resque.sort()
    max_p = resque[-1]
    min_p = resque[0]
    answer = 0
    # 시작위치 가장 큰경우
    if S >= max_p: answer = abs(S - resque[0])
    # 시작위치 가장 작은 경우
    elif S <= min_p: answer = abs(S - resque[-1])
    # 중간인 경우
    else:
        left = abs( S - resque[0])
        right = abs( S - resque[-1])
        if left >= right: answer = right + left + right
        else: answer = left + right + left
    print('#{} {}'.format(test_case, answer))


"""


"""
############ 2번 풀이

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 1번 팀원부터 시작이므로 인덱스 떄문에 0 추가 ( 0~N 까지 존재 )

    # 현재값
    score = [0] + list(map(int, input().split()))
    total_sum = sum(score)

    # 목표값
    target = [ max(score[i] + i , i) for i in range(N+1)]


    print(score)
    print(target)
    data = [ b - a for a, b in zip(score, target) ]  # 증가폭 데이터
    print(data)
    data.sort(reverse= True)


    cnt = 0
    for i in data:
        if total_sum >= 2 * N: break
        total_sum += i
        cnt += 1
    print(cnt)
    print('-------------------')

"""