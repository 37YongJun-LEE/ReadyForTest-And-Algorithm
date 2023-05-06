# 정답 풀이
def check_cnt(a, b, N):
    global answer
    prev_row = data[a][0]
    prev_col = data[0][b]
    cnt = 1
    for i in range(1, N):
        if data[a][i] == prev_row:
            cnt += 1
        else:
            cnt = 1
            prev_row = data[a][i] # 이전 내용 저장하기
        answer = max(answer, cnt)
    cnt = 1
    for j in range(1, N):
        if data[j][b] == prev_col:
            cnt += 1
        else:
            cnt = 1
            prev_col = data[j][b]
        answer = max(answer, cnt)
    return

dx = [-1, 0, 1, 0] # 상 하
dy = [0, -1, 0, 1] # 좌 우

T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(input()))

    for i in range(N):
        check_cnt(i, i, N)

    for x in range(N):   # 행,
        for y in range(N):  # 열,
            for i in range(4): # 첫번째 고른 색,
                x1 = x + dx[i]
                y1 = y + dy[i]
                if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N:
                    x1 = x - dx[i]
                    y1 = y - dy[i]
                    continue # 해당 범위이면 거르기
                if data[x1][y1] != data[x][y]:#색이 다른 경우에만 두 색 변경
                    data[x1][y1], data[x][y] = data[x][y], data[x1][y1]
                    check_cnt(x1, y1, N)
                    check_cnt(x, y, N)
                    data[x1][y1], data[x][y] = data[x][y], data[x1][y1]
    print('#{} {}'.format(test_case, answer))


"""

1
5
BYRBG
YRYGB
RBRYY
BGYBG
BGYGR
"""




"""
# 처음 풀때 설명과 초기 코드 ;:    
#-해당 코드 ㄹ틀림 문제 잘못읽음..... 인접한 상하좌우중에서 2개 고르는 것이 아니라 ,,, 인접한! 즉 상하좌우에서 색이 다른 인접하고있는 두칸을 고르는것,
 # 즉 상과 본인, 하와 본인, 좌와 본인, 우와 본인 이런식.... 내가 이상한가? 진짜로 문제가 헷갈리게 적혀있다.
def check_cnt(a, b, N):
    # 행에서 연속 같은 색 개수 탐색
    global answer
    prev_row = data[a][0]
    prev_col = data[0][b]
    # 해당 행 탐색
    cnt = 1
    for i in range(1, N):
        if data[a][i] == prev_row:
            cnt += 1
        else:
            cnt = 1
            prev_row = data[a][i] # 이전 내용 저장하기
        answer = max(answer, cnt)
    # 해당 열 탐색
    cnt = 1
    for j in range(1, N):
        print(data[j][b])
        if data[j][b] == prev_col:
            cnt += 1
        else:
            cnt = 1
            prev_col = data[j][b]
        answer = max(answer, cnt)
    return


 # 헷갈리니까 반시계방향 탐색순으로 나오게 세팅
dx = [-1, 0, 1, 0] # 상 하
dy = [0, -1, 0, 1] # 좌 우

T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(input()))

    # 첫줄부터 하나씩 돌면서. 탐색하기 4방향
    for x in range(N):   # 행,
        for y in range(N):  # 열,
            #print(data[x][y])
            # 해당 [x][y]에서 4방향 탐색, and 한 방향과 다른 방향 색 다르면 변경시키기
            for i in range(4): # 첫번째 고른 색,
                x1 = x + dx[i]
                y1 = y + dy[i]
                if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N:
                    x1 = x - dx[i]
                    y1 = y - dy[i]
                    continue # 해당 범위이면 거르기

                for j in range(i,4): # 2번째 다른 색
                    x2 = x + dx[j]
                    y2 = y + dy[j]
                    if x2 < 0 or y2 < 0 or x2 >= N or y2 >= N:# 해당 범위이면 거르기
                        x2 = x - dx[j]
                        y2 = y - dy[j]
                        continue

                    # 두 색 변경
                    if data[x1][y1] != data[x2][y2]:#색이 다른 경우에만 두 색 변경
                        print(x, y, data[x][y])
                        print(x1, y1, '::', x2, y2)
                        print(data[x1][y1], data[x2][y2])
                        data[x1][y1], data[x2][y2] = data[x2][y2], data[x1][y1]

                        for k in range(N):
                            print(data[k])

                        # 변경된 행과 열 탐색
                        check_cnt(x1, y1, N)
                        check_cnt(x2, y2, N)

                        print(answer)
                        print('-------------------------')

                        # 원상복귀 시켜주기.
                        data[x1][y1], data[x2][y2] = data[x2][y2], data[x1][y1]

    print('#{} {}'.format(test_case, answer))

"""


"""
################################################# 해당좌표와 인접하고 있는, 두개의 서로 다른색의 칸을 교환하는 코드 
def check_cnt(a, b, N):
    global answer
    prev_row = data[a][0]
    prev_col = data[0][b]
    cnt = 1
    for i in range(1, N):
        if data[a][i] == prev_row:
            cnt += 1
        else:
            cnt = 1
            prev_row = data[a][i] # 이전 내용 저장하기
        answer = max(answer, cnt)
    cnt = 1
    for j in range(1, N):
        if data[j][b] == prev_col:
            cnt += 1
        else:
            cnt = 1
            prev_col = data[j][b]
        answer = max(answer, cnt)
    return

dx = [-1, 0, 1, 0] # 상 하
dy = [0, -1, 0, 1] # 좌 우

T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(input()))

    for i in range(N):
        check_cnt(i, i, N)

    for x in range(N):   # 행,
        for y in range(N):  # 열,
            for i in range(4): # 첫번째 고른 색,
                x1 = x + dx[i]
                y1 = y + dy[i]
                if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N:
                    x1 = x - dx[i]
                    y1 = y - dy[i]
                    continue # 해당 범위이면 거르기
                for j in range(i,4): # 2번째 다른 색
                    x2 = x + dx[j]
                    y2 = y + dy[j]
                    if x2 < 0 or y2 < 0 or x2 >= N or y2 >= N:# 해당 범위이면 거르기
                        x2 = x - dx[j]
                        y2 = y - dy[j]
                        continue
                    if data[x1][y1] != data[x2][y2]:#색이 다른 경우에만 두 색 변경
                        data[x1][y1], data[x2][y2] = data[x2][y2], data[x1][y1]
                        check_cnt(x1, y1, N)
                        check_cnt(x2, y2, N)
                        data[x1][y1], data[x2][y2] = data[x2][y2], data[x1][y1]
    print('#{} {}'.format(test_case, answer))

"""