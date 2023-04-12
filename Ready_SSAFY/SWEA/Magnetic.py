T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////


    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    for i in range(100):
        prev = 0

        for j in range(100):
            now = data[j][i]
            if now == 1:
                prev = 1

            if prev == 1 and now == 2:
                answer += 1
                prev = 0
    print('#' + str(test_case), answer)
    # ///////////////////////////////////////////////////////////////////////////////////
