n = int(input())
data = list(map(int, input().split()))

count = 0
data.sort()



while True:
    n = n - data[-1]
    count += 1
    data.pop()

    if data[-1] <= n:
        count += 1
        break

print(count)