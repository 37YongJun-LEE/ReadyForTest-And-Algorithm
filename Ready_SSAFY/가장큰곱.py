def check(x):
    prev = x % 10
    x = x // 10
    while x > 0:
        if x % 10 != prev - 1 : return False
        prev = x % 10
        x = x // 10
    return True

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    flag = False
    answer = 0
    for a in range(N):
        for b in range(a+1, N):
            # 계단수 판별
            if check(data[a]*data[b]):
                answer = max(answer, data[a]*data[b])

    if not answer: print('#{} {}'.format(test_case, -1))
    else: print('#{} {}'.format(test_case, answer))












"""
# 문제 핵심 : 계단수 판별을 어떻게 구현할 것인가? -> 알고있는게 좋다. 10으로 %, //, 나누어서 나머지가 1씩 감소하는 경우를 확인

### 정답풀이
T = int(input())
def check(x):
    prev = x % 10
    x = x // 10
    while x > 0:
        if x % 10 != prev - 1: return False
        prev = x % 10
        x = x // 10
    return True

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        for j in range(i + 1, N):
            if check(data[i] * data[j]):
                answer = max(answer, data[i] * data[j])
    if answer == 0: answer = -1
    print('#{} {}'.format(test_case, answer))

"""



"""
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    combi = []
    for i in range(N):
        for j in range(i + 1, N):
            combi.append(data[i] * data[j])

    combi.sort()
    print('#{} {}'.format(test_case, combi))
"""

"""
10
7
3 24 24 27 3 16 29
7
14 28 5 22 18 20 16
7
17 22 7 10 9 29 11
9
8 13 18 30 11 14 6 11 10
10
4 7 7 9 8 1 20 16 28 5
8
4 26 5 2 18 17 11 24
9
10 15 23 6 8 3 27 4 2
10
6 5 23 26 11 27 15 18 25 12
6
27 1 14 25 8 21
8
11 5 8 28 30 13 24 12


"""
