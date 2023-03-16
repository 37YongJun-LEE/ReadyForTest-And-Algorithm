import sys

n, k = map(int, input().split())

array1 = list(map(int, sys.stdin.readline().split()))
array2 = list(map(int, sys.stdin.readline().split()))

array1.sort()
array2.sort(reverse=True)
cnt = 0
for i in range(n):
    cnt += 1
    if array1[i] < array2[i]:
        array1[i], array2[i] = array2[i], array1[i]


    if cnt == k:
        break

print(sum(array1))