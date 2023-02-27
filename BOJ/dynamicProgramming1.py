# 바텀 업 방식 구현

n = int(input())


d = [0]*n

d[1] = 1

for i in range(2,n+1):
    d[i] = d[i-1]