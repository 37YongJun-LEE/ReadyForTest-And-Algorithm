import sys
from collections import deque

n = int(input())
NGE_queue = deque(map(int, sys.stdin.readline().split()))
queue = deque()

for i in range(len(NGE_queue)):
    if not NGE_queue:
        break
    queue = list(NGE[i+1:])
    while NGE[i] < queue[0]:
        queue.popleft()
    print(queue[0], end=' ')
