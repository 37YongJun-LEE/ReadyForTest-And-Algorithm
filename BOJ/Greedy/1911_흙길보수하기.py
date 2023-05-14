import sys
input = sys.stdin.readline
n, L = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(n)]
# 웅덩이 좌표 오름차순 정렬
pools.sort(key=lambda x:x[0])

# 웅덩이를 덮은 마지막 널빤지의 위치
cur = 0
# 널빤지의 개수
cnt = 0
for start, end in pools:
    if start > end:
        continue
    # 이전 웅덩이에서 덮은 널빤지가 해당 웅덩이를 덮고있는 경우
    if cur > start:
        start = cur
    # 널빤지의 개수 카운트
    while start < end:
        start += L
        cnt += 1
    cur = start

print(cnt)


"""
N, L = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(1, N+1)]
# 정렬필요
data.sort()

prev_ws = 0
prev_we = 0
total = 0
prev_plate = 0
now_plate = 0
cnt = 0

for ws, we in data:
    # 겹치는 경우 ( 겹치는 모든 경우 포괄 ) + L-2 차이만 나는경우
    if prev_ws != 0 and prev_we != 0 and ws - prev_we <= L-2:
        print('겹치는경우')
        s = min(prev_ws, ws)
        e = max(prev_we, we)
        total -= prev_plate
        if (e - s) % L == 0:
            now_plate = (e - s) // L
        else:
            now_plate = (e - s) // L + 1

    # 안겹치는 경우
    else:
        print('안겹치는경우')
        if (we - ws) % L == 0:
            now_plate = (we - ws) // L
        else:
            now_plate = (we - ws) // L + 1

    total += now_plate
    prev_plate = now_plate
    prev_we = we
    prev_ws = ws
    print('---------------')

print(total)

"""


