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

