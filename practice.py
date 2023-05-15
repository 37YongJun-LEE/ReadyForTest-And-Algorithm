from collections import deque

T = int(input())
for test_case in range(1, T+1):
    data = list( deque(input()) for i in range(5) )
    print('#{}'.format(test_case), end = ' ')
    while data:
        empty = 0
        for i in range(5):
            if not data[i]:
                empty += 1
                continue

            a = data[i].popleft()
            print(a, end='')

        if empty == 5:
            break
    print()



"""
2
ABCDE
abcde
01234
FGHIJ
fghij
1
AABCDD
afzz
09121
a8EWg6
P5h3kx
"""


"""T = int(input())
for test_case in range(1, T+ 1):
    N = int(input())
    score = [0]+list(map(int, input().split()))
    now_sum = sum(score)
    up_score = []
    for i in range(N+1):
        up_score.append(max(score[i] + i, i))
    # 증가폭 데이터 따로 저장
    data = []
    for a, b in zip(score, up_score):
        data.append(b-a)
    data.sort(reverse= True)
    cnt = 0
    for i in data:
        if now_sum >= 2 * N: break
        now_sum += i
        cnt += 1
    print('#{} {}'.format(test_case, cnt))
"""
"""N = int(input())
timeline = []
for i in range(N):
    s, e = map(int, input().split())
    timeline.append( [e, s] )
timeline.sort()

prev_end = 0
cnt = 0
for e, s in timeline:
    if prev_end > s:
        continue
    else:
        cnt += 1
        prev_end = e
print(cnt)"""

"""N = int(input())
data= list(map(int, input().split()))

data.sort()
max_data = data.pop()
sum_data = sum(data)
answer = 0
if max_data >= sum_data:
    answer = max_data - sum_data
else:
    while max_data < sum_data:
        if max_data == sum_data:
            break
        max_data -= 1
        sum_data -= 2
    answer = max_data - sum_data

print(answer)

"""


"""
N = int(input())
data =list(map(int, input().split()))
even_idx = []
# 짝수의 인덱스가 필요하다 0 2 4... 와의 거리를 차례로 보기위해서.
for i in range(N):
    if data[i] % 2 == 0:
        even_idx.append(i)

x = 0               # 0 1 0 1 0 1 ...
for i in range(len(even_idx)): # 0 2 4 6 ....
    x += abs(even_idx[i] - (2*i) )


y = 0               # 1 0 1 0 1 0 ...
for i in range(len(even_idx)): # 1 3 5 7 ....
    y += abs(even_idx[i] - (2*i+1))


if N % 2 != 0: # 길이 홀수이면
    if len(even_idx) % 2 == 0:
        x = y
    else:
        y = x

answer = min(x, y)
print(answer)"""