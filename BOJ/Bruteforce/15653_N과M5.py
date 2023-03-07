import itertools
from itertools import *

n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()


data = itertools.permutations(num, m)


for i in data:
    for j in i:
        print(j, end=' ')
    print()
