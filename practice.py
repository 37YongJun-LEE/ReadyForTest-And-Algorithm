T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 매년 N개 만큼 나누어줄수 있다.
    now_candy = list(map(int, input().split()))

    total = sum(now_candy)
    cnt = 1
    while total < N:
        cnt += 1
        total += 3 * total

    print(cnt)






"""T = int(input())
for test_case in range(1, T + 1):
    number = list( map(int, list(input())) )
    l = len(number)
    cnt = 0
    while number[::-1] != number:
        number[-1] += 1

        for i in range(l-1, 0, -1):
            if number[i] == 10:
                number[i] = 0
                number[i-1] += 1
a        cnt += 1
    print('#{} {}'.format(test_case, cnt))
"""

"""T = int(input())
for test_case in range(1, T + 1):
    number = list( map(int, list(input())) )

    print(number)
    cnt= 0
    while number[::-1] != number:
        number[-1] += 1
        for i in range(len(number)-1, 0, -1):
            if number[i] == 10:
                number[i] = 0
                number[i-1] += 1
        cnt += 1

    print(cnt)

"""


"""dx = [-1, +1, 0, 0] #행: 상 하 좌 우
dy = [0, 0, -1, +1] # 열

def check(x, y, LRUD):
    nx = x + dx[LRUD]
    ny = y + dy[LRUD]
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return False

    if data[x][y] != data[nx][ny]:
        return True
    else:
        return False

def count(x, y):
    answer = 0
    # 가로 경우
    x_cnt = 1
    prv_x = ''
    for x1 in data[x]:
        if x1 != prv_x: # 다른경우
            x_cnt = 1
        else: # 같은경우
            x_cnt += 1
        prv_x = x1
        answer = max(x_cnt, answer)

    y_cnt = 1
    prv_y = ''
    for i in range(N):
        if data[i][y] != prv_y:
            y_cnt = 1
        else:
            y_cnt += 1
        prv_y = data[i][y]
        answer = max(y_cnt, answer)
    return answer

# 가장 긴 바둑돌
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list( list(input()) for _ in range(N))

    answer = 0
    for l in range(N):
        answer = max(answer, count(l, l))

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if check(i, j, k):
                    # 변경 가능하다면 바꾸기
                    data[i][j], data[i + dx[k]][j + dy[k]] = data[i + dx[k]][j + dy[k]], data[i][j]

                    answer = max(answer, count(i, j))
                    answer = max(answer, count(i + dx[k], j + dy[k]))

                    # 원상복귀
                    data[i][j], data[i + dx[k]][j + dy[k]] = data[i + dx[k]][j + dy[k]], data[i][j]

    print(answer)
"""
"""
5
5
BYRBG
YRYGB
RBRYY
BGYBG
BGYGR
6
YRGRRR
BYGGRR
RBBGBR
RBRRGB
RGBYRY
GYGYGG
3
BRG
GGG
BYG
5
GGYBY
BRBBY
YRBBR
RBRYG
GRYYY
4
GYBR
YYGY
BBYR
YBYR

"""


"""T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    triangle = []
    for i in range(N):
        triangle.append([1] * (i+1))

    for i in range(N):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    print('#{}'.format(test_case))
    for i in range(N):
        for k in triangle[i]:
            print(k, end = ' ')
        print()
"""
"""
####### 파이널 캠프 C 2번 망설임
def check(x):
    visited[x] = True

    while True:
        idx = -1  ## 가장 가까운 친구와의 좌표
        d = 5000  ## 가장 가까운 친구와의 거리

        for i in range(N):
            if data[i] == 'o' and not visited[i]:
                # 현재위치 x 와 모든 i 사이의 거리를 구해서 가장 거리가 작은 경우에 ok
                if abs(x-i) < d: # 그치 현재 계산한 거리가 d 보다 작은 경우에 갱신되어야지
                    d = abs(x-i) # 거리 갱신
                    idx = i # 좌표 갱신
                elif d == abs(x-i): # 만약 거리가 같은 경우가 있다면 False
                    return False

        if idx == -1: # idx가 -1인 경우는 모든 위치를 방문한 경우 따라서 전체 반복문 탈출
            break

        x = idx
        visited[x] = True

    return True

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(input())
    cnt = 0
    for i in range(N):
        visited = [False] * N
        if check(i):
            cnt += 1

    print('#{} {}'.format(test_case, cnt))
"""


"""from collections import deque

T = int(input())
for test_case in range(1, T+1):
    data = list( deque(input()) for i in range(5) )
    print('#{}'.format(test_case), end = ' ')
    while data:
        empty = 0
        for i in range(5):
            if not data[i]:
                empty += 1
                continue

            a = data[i].popleft()
            print(a, end='')

        if empty == 5:
            break
    print()

"""

"""
2
ABCDE
abcde
01234
FGHIJ
fghij
1
AABCDD
afzz
09121
a8EWg6
P5h3kx
"""


"""T = int(input())
for test_case in range(1, T+ 1):
    N = int(input())
    score = [0]+list(map(int, input().split()))
    now_sum = sum(score)
    up_score = []
    for i in range(N+1):
        up_score.append(max(score[i] + i, i))
    # 증가폭 데이터 따로 저장
    data = []
    for a, b in zip(score, up_score):
        data.append(b-a)
    data.sort(reverse= True)
    cnt = 0
    for i in data:
        if now_sum >= 2 * N: break
        now_sum += i
        cnt += 1
    print('#{} {}'.format(test_case, cnt))
"""
"""N = int(input())
timeline = []
for i in range(N):
    s, e = map(int, input().split())
    timeline.append( [e, s] )
timeline.sort()

prev_end = 0
cnt = 0
for e, s in timeline:
    if prev_end > s:
        continue
    else:
        cnt += 1
        prev_end = e
print(cnt)"""

"""N = int(input())
data= list(map(int, input().split()))

data.sort()
max_data = data.pop()
sum_data = sum(data)
answer = 0
if max_data >= sum_data:
    answer = max_data - sum_data
else:
    while max_data < sum_data:
        if max_data == sum_data:
            break
        max_data -= 1
        sum_data -= 2
    answer = max_data - sum_data

print(answer)

"""


"""
N = int(input())
data =list(map(int, input().split()))
even_idx = []
# 짝수의 인덱스가 필요하다 0 2 4... 와의 거리를 차례로 보기위해서.
for i in range(N):
    if data[i] % 2 == 0:
        even_idx.append(i)

x = 0               # 0 1 0 1 0 1 ...
for i in range(len(even_idx)): # 0 2 4 6 ....
    x += abs(even_idx[i] - (2*i) )


y = 0               # 1 0 1 0 1 0 ...
for i in range(len(even_idx)): # 1 3 5 7 ....
    y += abs(even_idx[i] - (2*i+1))


if N % 2 != 0: # 길이 홀수이면
    if len(even_idx) % 2 == 0:
        x = y
    else:
        y = x

answer = min(x, y)
print(answer)"""