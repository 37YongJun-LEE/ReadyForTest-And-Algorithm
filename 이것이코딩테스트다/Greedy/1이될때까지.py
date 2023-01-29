n, k = map(int, input().split())

# n 에서 -1 하기
# -1 된 n 을 k 로 나누기 => 반복
count = 0

while n != 1:

    if n % k == 0:
        n = n // k
        count += 1
    else:
        n = n-1
        count += 1

print(count)
