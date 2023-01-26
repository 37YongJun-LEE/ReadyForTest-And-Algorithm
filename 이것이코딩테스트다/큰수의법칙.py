n, m, k = map(int, input().split()) # n=5, m=8, k=3
                                    # map은 지정된 함수를 각 변수에 할당해 적용해 주는 함수

data = list(map(int, input().split()))  # [2,4,5,4,6]

# 아이디어 1 . 가장큰수와 그다음 큰수를 저장하면 문제는 쉽게 풀릴것이다.
# n개의 정수, 총 m번 더해야할 때, 연속 가능한 횟수는 k

data.sort()
set(data)
highest = data[-1]
next_high = data[-2]

answer = 0

for i in range(1, m+1):
    if i != 1 and i % k == 1:
        answer += next_high
    else:
        answer += highest


print(answer)





