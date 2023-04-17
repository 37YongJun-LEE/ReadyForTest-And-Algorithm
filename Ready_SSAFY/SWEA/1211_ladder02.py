# 최단경로 카운팅 추가 완료. 매커니즘에 이상 없음
# 결국 아래로 내려가는 건 모두 100칸으로 동일하니까. 가로 이동만 카운팅해서 계산

# 왼쪽 오른쪽 판별후 이동. 이동한 다음 좌표 리턴. 완성
def LR_search(y, x, cnt):    # data[y][x]    왼쪽 오른쪽 둘다 없으면 자기자신 리턴, 있으면 이동 후 좌표 리턴
    if 0 < x < 99:
        if data[y][x-1] == 1: # 왼쪽
            x -= 1
            while data[y+1][x] != 1: # 맨 왼쪽의 아래가 1이 나올때까지.( 세로줄 만날때까지...)
                x -= 1
                cnt += 1
                if x == 0:
                    break
            return (y, x, cnt)

        elif data[y][x+1] == 1: # 오른쪽
            x += 1
            while data[y+1][x] != 1:  # 맨 오른쪽 아래가 1이 나올때까지 ( 세로줄 만날때까지...)
                x += 1
                cnt += 1

                if x == 99:
                    break
            return (y, x, cnt)
        else:
            return (y, x, cnt)

    elif x == 0:
        if data[y][x + 1] == 1:  # 오른쪽
            x += 1
            while data[y + 1][x] != 1:  # 맨 오른쪽 아래가 1이 나올때까지 ( 세로줄 만날때까지...)
                x += 1
                cnt += 1

                if x == 99:
                    break
        return (y, x, cnt)

    elif x == 99:
        if data[y][x-1] == 1: # 왼쪽
            x -= 1
            while data[y+1][x] != 1: # 맨 왼쪽의 아래가 1이 나올때까지.( 세로줄 만날때까지...)
                x -= 1
                cnt += 1

                if x == 0:
                    break
        return (y, x, cnt)

    else:
        return (y, x, cnt)

# 진행방향 함수
def down(y, x):   # data[y][x]
    cnt = 0
    while True:
        y, x, cnt = LR_search(y, x, cnt)
        y += 1

        #print(y,x)
        if y == 99:
            break

    return y, x, cnt


### 풀이 시작
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())
    data = [ list(map(int, input().split())) for _ in range(100)]
    #print(data)

    start_point = []

    for i in range(100):
        if data[0][i] == 1:
            start_point.append(i)

    now_cnt = 10000

    for i in start_point:

        y, x, cnt = down(0, i)

        if cnt < now_cnt:
            now_cnt = cnt

            answer = i

    print( '#' + str(tc), answer)
"""
# test
3
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
"""


""" ## 6,1 테스트
### 0 1 2 3 4 5 6 7 8 9 x 
#y
0   1 0 0 0 1 0 1 0 0 1     
1   1 0 0 0 1 0 1 1 1 1
2   1 0 0 0 1 0 1 0 0 1
3   1 0 0 0 1 1 1 0 0 1
4   1 0 0 0 1 0 1 0 0 1
5   1 1 1 1 1 0 1 1 1 1
6   1 0 0 0 1 0 1 0 0 1
7   1 1 1 1 1 0 1 0 0 1
8   1 0 0 0 1 1 1 0 0 1
9   1 0 0 0 1 0 1 0 0 1

"""