import sys
from collections import deque

n = int(input())
NGE = deque(map(int, sys.stdin.readline().split()))

# 오른쪽 큰 수, 없으면 -1

answer = []

while NGE:
    k = NGE[0]
    NGE.popleft()
    if len(NGE) == 0 or k >= max(NGE):
        answer.append(-1)
        continue
    for i in NGE:
        if k < i:
            answer.append(i)
            break
        else:
            continue

for j in answer:
    print(j, end=' ')