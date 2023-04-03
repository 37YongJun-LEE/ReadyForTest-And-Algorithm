import sys
n, m = map(int, input().split())
ball = list(map(int, sys.stdin.readline().split()))

# 1. 먼저 무게가 1~10이라고 고정되어 있으므로 리스트에 각 무게에 해당하는 공의 개수를 세어준다
array = [0] * 11 # 1부터 10까지의 무게의 공

for i in range(len(ball)):
    array[ball[i]] += 1

# 2. 서로 다른 무게의 공 개수들이 카웉트 되었으므로 최종 조합 수를 계산한다.
answer = 0
# 1부터 m까지의 무게 처리
for i in range(1, m+1):
    n -= array[i]       # 무게가 i인 볼링공의 개수 제외
    answer += array[i] * n   # B가 선택하는 경우의 수와 곱하기

print(answer)



"""
from collections import deque
import sys

n, m = map(int, input().split())
ball = deque(map(int, sys.stdin.readline().split()))
answer = 0
while True:
    a = ball.popleft()

    for i in ball:
        if a != i:
            answer += 1

    if len(ball) == 1:
        break
print(answer)

"""



"""
# taskcase
8 5
1 5 4 3 2 4 5 2

"""