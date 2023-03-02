import sys
from collections import deque

n = int(input())

k = deque(map(int, sys.stdin.readline().split()))
k.appendleft(0)

d = [0] * (n+1)
d[1] = k[1]

for i in range(1, n+1):
    if i % 2 != 0:  # 홀수면
        d[i] = max(d[1] + d[i-1], k[i])
    else:   # 짝수면
        d[i] = max(d[1] + d[i-1], k[i//2]*2, k[i])

print(d[n])