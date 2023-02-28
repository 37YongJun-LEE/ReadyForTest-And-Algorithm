from itertools import *

# len()이 n 인 리스트 만들기

# 재귀를 쓰지않고 메모리에 계산 값을 저장한것을 호출하여 부르기
# 주로 점화식이 나타날때 dp를 사용한다.
# 점화식: 인접한 3항간의 연관 관계를 표현한 식

n = int(input())
tile = [0]*(n+2)


tile[1] = 1
tile[2] = 2

for i in range(2, n+1):
    if tile[i] != 0:
        continue
    else:
        tile[i] = tile[i-1] + tile[i-2]


print(tile[n] % 10007)


