
n = int(input())
tile = [0]*(n+2)


tile[1] = 1
tile[2] = 3

for i in range(2, n+1):
    if tile[i] != 0:
        continue
    else:
        tile[i] = tile[i-1] + tile[i-2]*2


print(tile[n] % 10007)
