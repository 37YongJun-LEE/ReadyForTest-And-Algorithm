# 다시 풀기 한번더
# dfs 사용.
def dfs(dataindex, taste_sum, kcal_sum):
    global max_taste_sum
    # 현재 칼로리 합이 L 보다 크면 계산 x , dfs 종료
    if kcal_sum > L: return
    # 칼로리 총합이 기존 최대보다 크면 최댓값 갱신
    if max_taste_sum < taste_sum:
        max_taste_sum = taste_sum
    # 현재 인덱스가 N 이면 탈출 dfs 종료 (총 재료 다씀)
    if dataindex == N: return
    # 현재 재료의 맛점수와 칼로리 받아오기
    taste, kcal = data[dataindex]
    # 다음 재료의 사용 유무로 넘기기
        # 현 재료 사용한 경우
    dfs(dataindex + 1, taste_sum + taste, kcal_sum + kcal)
        # 현 재료 사용 안한 경우
    dfs(dataindex+1, taste_sum, kcal_sum)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, L = map(int, input().split())    # N 재료 개수, L 칼로리 총합 제한
    data = [tuple(map(int, input().split()) ) for _ in range(N) ]

    max_taste_sum = 0
    dfs(0, 0, 0) # 현재 재료 인덱스, 맛 점수 총합, 칼로리 총합

    print("#{} {}".format(test_case, max_taste_sum))








##############################################################################
"""
# DFS를 이용한 방법
def dfs( dataindex, total_taste, total_kcal):
    global max_taste
    # 칼로리합 L 보다 큰 경우 리턴
    if total_kcal > L:
        return
    # max_taste 갱신
    if max_taste < total_taste:
        max_taste = total_taste
    # 사용 재료 개수가 N 을 넘어가는 경우 리턴
    if dataindex == N:
        return
    taste, kcal = data[dataindex]
    # 현 재료 사용된 경우
    dfs(dataindex+1, total_taste + taste, total_kcal + kcal)
    # 현 재료 사용 안된 경우
    dfs(dataindex+1, total_taste, total_kcal)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # 재료 개수 N, 칼로리 제한 L
    data = [tuple(map(int, input().split())) for i in range(N)]
    #print(data)
    max_taste = 0
    dfs(0, 0, 0)
    print(max_taste)
"""
############################################################################################################################################################

"""
# 조합을 이용한 완전탐색 방법
# 앞으로는 itertools 쓰지 말자. 많은 시험에서 itertools 사용을 제한하고 있다. 
# 좋은 풀이로 잘 연결되지도 않는다.

import itertools
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # 재료 개수 N, 칼로리 제한 L

    data = [tuple(map(int, input().split())) for i in range(N)]

    # print(data)
    answerlist = []

    for i in range(1, N + 1):
        combi = itertools.combinations(data, i)
        # print('# i=' , i , '인경우')

        # 칼로리 제한 L 에 맞는 경우의 수만 출력
        for j in combi:  # i인 경우의 조합들 순서대로
            taste_sum = 0
            cal_sum = 0
            # print(j)
            for k in j:
                # print(k)

                taste, cal = k
                taste_sum += taste
                cal_sum += cal

            # print(taste_sum, cal_sum)
            if cal_sum <= L:
                answerlist.append(taste_sum)

    print('#' + str(test_case), max(answerlist))
"""