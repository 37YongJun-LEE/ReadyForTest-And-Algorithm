import sys
from collections import deque

n = int(input())

k = deque(map(int, sys.stdin.readline().split()))
k.appendleft(0)

d = [0] * (n+1)
d[1] = k[1]

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j] + k[j])

print(d[n])