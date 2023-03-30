
import sys

## 금광문제 책 이코테

case = int(input())

for c in range(case):
    n, m = map(int, input().split())
    array = [ i for i in map(int, sys.stdin.readline().split() )]


    # 2차원 dp 초기화
    dp = []
    index = 0

    for i in range(n): # 2차원 배열이니 행 개수만큼 행 추가
        dp.append(array[index:index+m]) # 슬라이싱이용해서 append 해준다
        index += m


    # 마지막 열에서 답이 나오므로, 열이 증가할 때마다, 행에 대한 계산이 진행되는 것 기준으로 작성
    for j in range(1, m):
        for i in range(n):
            # 범위를 벗어나면 계산에 포함시킬 필요가 없으므로 행인 i를 벗어나느냐 마는냐가 포인트
            # 행 i가 0(첫행)인 경우에는 왼쪽위가 없으므로 왼쪽위 0 처리후 계산
            # 행 i가 n-1(마지막행) 경우에는 왼쪽 아래가 없으므로 왼쪽아래 0 처리 후 계산
            if i == 0 :
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            left = dp[i][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][i-1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)



    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1]) # 각 행의 맨 마지막 열에 있는 항의 집합들중 최댓값이 정답
    print(result)




"""

import sys

case = int(input())

for c in range(case):
    n , m = map(int, input().split())
    case = [ i for i in map(int, sys.stdin.readline().split()) ]

    dp = []
    index = 0
    for i in range(n):
        dp.append( case[index:index+m] )
        index += m

    print(dp)

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)


    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)

"""




"""
# taskcase
2
3 4
1 2 3 4 1 2 3 4 1 2 3 4
3 4
1 2 3 4 1 2 3 4 1 2 3 4
"""

"""
2
3 4 
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

"""
