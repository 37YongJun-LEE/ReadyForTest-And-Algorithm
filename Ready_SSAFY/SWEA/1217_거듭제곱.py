def prime(n, k, result):
    result = result * n
    if k == 1:
        return result
    else:
        return prime(n, k - 1, result)


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())
    n, k = map(int, input().split())
    answer = prime(n, k, 1)

    print('#' + str(tc), answer)
