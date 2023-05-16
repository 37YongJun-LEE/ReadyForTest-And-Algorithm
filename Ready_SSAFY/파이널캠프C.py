"""## 2
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    friend_line = list(input())
    print(friend_line)

    for i in range(N): # 시작 위치 0 부터 N-1 까지 완탐
        start = i

"""
"""
v = []
for _ in range(M): # 좌표 모두 v에 저장 입력
    a, b = map(int, input().split())
    v.append([a,b])
"""
"""
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    v = list( list(map(int, input().split())) for _ in range(M))

    # x 이동거리 최소, x 이동거리 최대
    min_x = N
    max_x = 1
    min_y = N
    max_y = 1

    for i in v:
        x = i[0]
        y = i[1]

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    dx = min(max_x - 1, N - min_x)
    dy = min(max_y - 1, N - min_y)

    if min_x == max_x:
        dx = 0
    if min_y == max_y:
        dy = 0
    print('#{} {}'.format(test_case, dx+dy))
"""


"""
############# 1번문항 풀이 코드
마법사 유니의 체스판
T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    v = [list(map(int, input().split())) for i in range(m)]

    mnx = n 
    mxx = 1
    mny = n
    mxy = 1
    
    # v = [ [a,b] , [c,d] .... [x, y] ]
    for i in v: 
        x = i[0]
        y = i[1]
    
        mnx = min(mnx, x)
        mxx = max(mxx, x)
        mny = min(mny, y)
        mxy = max(mxy, y)
    
    dx = min(mxx - 1, n - mnx)
    dy = min(mxy - 1, n - mny)
    
    if mnx == mxx:
        dx = 0
    if mny == mxy:
        dy = 0
    
    print('#' + str(t) + ' ' + str(dx + dy))

"""



"""
################## 캠프 C 1번문항 내 풀이
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    if M == 1:
        print('#{} {}'.format(test_case, 0))
        continue

    x_data = []
    y_data = []
    for _ in range(M):
        x, y = map(int, input().split())
        x_data.append(x)
        y_data.append(y)

    data_4 = [(1, 1), (N,N), (1, N), (N,1)]
    answer = 10000
    for a, b in data_4:
        x_move = 0
        y_move = 0
        for x1, y1 in zip(x_data, y_data):
            x_move = max(x_move, abs(x1 - a))
            y_move = max(y_move, abs(y1 - b))
        answer = min(answer, x_move + y_move)
        print(answer)
    print('#{} {}'.format(test_case, answer))

"""






################### 2번문항 풀이
##### 망설임
def check(x):
    visited = [False for i in range(n)]
    visited[x] = True
    while True:
        idx = -1 # 가장 가까운 친구와의 좌표 초기값
        d = 10000000 # 그때의 거리 초기값
        for i in range(n): # 현재 위치 x 로 부터, 모든 'o' 친구위치의 거리를 계산하기 
            if s[i] == 'o' and not visited[i]: # 해당 위치가 o이고 방문기록이 없다면,
                # 현재 위치가 x 이고, 친구위치 i 와의 거리를 계산하는 경우
                if abs(i - x) < d:  # 거리 == abs(i - x) 가 d 보다 작다면, 지금까지 제일 가까운 것보다 가까운 경우를 찾은 것이므로,
                    idx = i         # 따라서 가장 가까운 좌표 변경
                    d = abs(i - x)   # 가장 가까운 경우와 거리도 갱신
                #인데, 만약에 가장 가까운 경우랑, 해당 차이가같은 경우가 존재한다면, 거리가 같은 경우가 2개이므로 False
                elif abs(i - x) == d:
                    return False

        if idx == -1: # idx == -1이란 말은 하나도 방문할 경우가 없다는 것, 따라서 모두 다 방문한 경우이므로 while 문 빠져나온다.
            break
    x = idx # 현재위치 갱신하기
    visited[x] = True # 위치 방문처리하기

    return True


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    s = input()

    cnt = 0
    for i in range(n):
        if check(i):
            cnt += 1
    print('#' + str(t) + ' ' + str(cnt))
