from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    tc = int(input())

    queue = deque(map(int, input().split()))

    while True:

        for i in range(1, 6):
            first = queue.popleft()
            # print(first, '-', i)

            if first - i <= 0:
                first = 0
                queue.append(first)
                break

            first -= i
            queue.append(first)
            # print(queue)

        if queue[-1] == 0:
            break

    print('#' + str(tc), end=' ')
    for i in queue:
        print(i, end=' ')
    print()
    # ///////////////////////////////////////////////////////////////////////////////////
