
"""
import sys
h = int(input())

triangle = []
triangle.append([])
for i in range(h):
    triangle.append(list(map(int, sys.stdin.readline().split())))

#print(triangle)

for i in range(2, h+1):
    #print(i, triangle[i])
    for j in range(i):

        if j == 0: # 맨 왼쪽인 경우
            left = 0
            right = triangle[i-1][j]

        elif j == i-1: # 맨 오른쪽인 경우
            left = triangle[i-1][j-1]
            right = 0

        else:  # 나머지 가운데인 경우들
            left = triangle[i-1][j-1]
            right = triangle[i-1][j]

        #print('현재 j =', j, '왼오', left, right)
        triangle[i][j] = triangle[i][j] + max(left, right)

print(max(triangle[h]))

"""

# 문제를 풀때 정확하게 분석하지 않는 경향이있다.
# 너무 직관적으로 풀려고하지말고
# 충분히 분석하고 시도해보고 그다음에 차근히 풀어나갈 수 있는 능력을 길러야한다. 
# 급하게 문제 분석이나 생각도 안하고 일단 적기 시작하면 아무 의미 없다.
# 주어진 상황이 어떻게 전개되는 지에 대한 사실 근거 정확한 분석 필요

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
            
        dp[i][j] = dp[i][j] + max(up_left, up)
        
print(max(dp[n-1]))

"""
# taskcase
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""