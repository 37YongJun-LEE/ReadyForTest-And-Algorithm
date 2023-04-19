
def dfs(index, now_sum):
    global answer_cnt
    #print('dfs( {} , {} )'.format(index, now_sum))

    if now_sum == K:
        answer_cnt += 1
        #print( '+1')
        return

    if index == N:
        return

    num = data[index]
    dfs(index+1, now_sum + num)
    dfs(index+1, now_sum)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # 주어진 자연수 N개, 목표합 K
    data = list(map(int, input().split()))  # 주어진 자연수 리스트
    # 목표 합 K는 반드시 1개 이상 사용해야함
    answer_cnt = 0
    dfs(0, 0)
    print('#{} {}'.format(test_case, answer_cnt))
