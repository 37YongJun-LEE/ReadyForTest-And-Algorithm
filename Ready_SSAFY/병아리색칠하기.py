T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    M = int(input())
    data = list(map(int, input().split()))
    answer = 0
    for i in range(1, M):  # data에 저장된 데이터 살펴보기
        answer = max(answer, (data[i] - data[i-1]) // 2)
    answer = max(answer, data[0] - 0)
    answer = max(answer, N - data[-1])
    print(answer)

"""
# 겹치면 안된다고 생각하고 코드를 짰다. 겹쳐도 된다. 그냥 모든 구간 커버하는 x 구하기 문제 
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    M = int(input())
    data = list(map(int, input().split()))

    for x in range(1, N): # 1부터 증가하며, x값 살펴보기
        cnt = 0
        for i in range(1, M): # data에 저장된 데이터 살펴보기
            if (data[i] - x) - (data[i-1] + x) == 1:
                # 마지막 까지 다 건드렸으면 x값 맞음
                if i == M-1:
                    print('찾았다 x: ', x)
                continue # 차가 1인 경우 가능 다음것 탐색

            else:
                break # 해당 x값 안되니 다음 x로 넘어가기

"""