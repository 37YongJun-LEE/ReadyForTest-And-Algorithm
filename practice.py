from collections import deque


def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        q = queue.popleft()
        seq = 0

        for i in queue:
            if q <= i:
                seq += 1
            else:
                seq += 1
                break
        answer.append(seq)
    return answer