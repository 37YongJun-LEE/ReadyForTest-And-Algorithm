T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    view = list(map(int, input().split()))

    answer = 0

    for i in range(2, n - 2):
        k = view[i]
        a = k - view[i - 2]
        b = k - view[i - 1]
        c = k - view[i + 1]
        d = k - view[i + 2]

        if a > 0 and b > 0 and c > 0 and d > 0:
            answer += min(a, b, c, d)
        else:
            continue

    print('#' + str(test_case), answer)
