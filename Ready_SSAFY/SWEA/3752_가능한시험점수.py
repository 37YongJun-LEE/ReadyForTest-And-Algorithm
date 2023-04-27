# 처음 시도한 것 처럼 dp 문제가 분명하다 그렇다면 어떻게 적용하는가?
    # 지금까지 만들어진 점수들을 다른 리스트에 넣고, 다시 새로운 점수 뽑을 때, 다 더해보기. dp로 중복 거르기
    
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 문제개수
    data = list(map(int, input().split())) # 문제 번호순 나열된 문제점수
    dp = [1] + [0] * sum(data)# 0 부터 총 합까지의 dp생성
    score_history = [0]
    for i in data:
        for j in range(len(score_history)):
            if dp[score_history[j] + i] == 0:
                dp[score_history[j] + i] = 1
                score_history.append(score_history[j] + i)
    print(sum(dp))

"""
# 이정도면 dfs 쓰지 말라는 문제.
# itertools 쓰면 그냥 풀리긴 할텐데..
def dfs(idx, data, cnt, total_score):
    global dp
    global answer
    if cnt == N:
        if dp[total_score] == 0:
            dp[total_score] = 1
            answer += 1
        return
    score = data[idx]   # 현재 문제 점수
    dfs(idx+1, data, cnt+1, total_score + score)    # 문제 맞춘경우
    dfs(idx+1, data, cnt+1, total_score)   # 문제 틀린경우

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 문제개수
    data = list(map(int, input().split())) # 문제 번호순 나열된 문제점수
    dp = [0] * ((N+1) * 100)
    answer = 0
    # dfs(idx, data, cnt, now_sum)
    dfs(0, data, 0, 0)
    print(answer)
"""
"""
#### 시간 초과 발생 : 논리랑 정답은 맞음

def dfs(idx, data, cnt, total_score):
    global dp
    if cnt == N:
        dp[total_score] = 1
        return total_score
    score = data[idx]   # 현재 문제 점수
    dfs(idx+1, data, cnt+1, total_score + score)    # 문제 맞춘경우
    dfs(idx+1, data, cnt+1, total_score)   # 문제 틀린경우

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 문제개수
    data = list(map(int, input().split())) # 문제 번호순 나열된 문제점수
    dp = [0] * (N * 100)
    # dfs(idx, data, cnt, now_sum)
    dfs(0, data, 0, 0)
    print(sum(dp))
"""
"""

2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1


1
3
2 3 5


"""