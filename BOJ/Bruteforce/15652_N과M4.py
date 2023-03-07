import itertools
from itertools import *

n, m = map(int, input().split())

num = []
for i in range(1,n+1):
    num.append(i)

data = itertools.combinations_with_replacement(num, m)

for i in data:
    for j in i:
        print(j, end=' ')
    print()