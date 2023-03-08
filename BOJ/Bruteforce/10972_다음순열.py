import itertools
from itertools import *

n = int(input())
num = list(map(int, input().split()))

num2 = num.copy()
num2.sort()

data = itertools.permutations(num2, n)

stack = []

for i in data:

    if i == tuple(num):
        stack.append(i)
        continue

    if stack:
        for j in i:
            print(j, end=' ')
        stack.pop()
        break
if stack:
    print(-1)
