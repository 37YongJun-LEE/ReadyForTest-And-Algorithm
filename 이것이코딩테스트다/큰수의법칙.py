n, m, k = map(int, input().split()) # n=5, m=8, k=3

data = list(map(int, input().split()))  # [2,4,5,4,6]

# 아이디어 1 . 가장큰수와 그다음 큰수를 저장하면 문제는 쉽게 풀릴것이다.
# n개의 정수, 총 m번 더해야할 때, 연속 가능한 횟수는 k

set(data)
data.sort()
highest = data[-1]
next_high = data[-2]

answer = 0

for i in range(1, m+1):
    if i % k == 1:
        answer += next_high
    else:
        answer += highest


print(answer)



