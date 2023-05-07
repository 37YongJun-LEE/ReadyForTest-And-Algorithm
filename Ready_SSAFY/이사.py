from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    stock = list(map(int, input().split()))

    box.sort()
    stock.sort()
    box_queue = deque(box)
    stock_queue = deque(stock)

    answer = 0
    cnt = 0
    while box_queue:
        while stock_queue and box_queue[0] > stock_queue[0]:
            cnt += 1
            stock_queue.popleft()
        answer += cnt
        box_queue.popleft()
    print('#{} {}'.format(test_case, answer))
