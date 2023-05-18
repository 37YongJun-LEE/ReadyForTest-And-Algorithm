from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    data = list(input().split())

    if N % 2 == 0:
        L = deque(data[:N//2])
        R = deque(data[N//2:])
    else:
        L = deque(data[:(N // 2)+1])
        R = deque(data[(N // 2)+1:])

    print('#{}'.format(test_case) , end=' ')
    answer = []
    while True:
        if not L and not R:
            break
        if L:
            l = L.popleft()
            print(l, end=' ')
        if R:
            r = R.popleft()
            print(r, end=' ')
    print()

"""


3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA	




 
"""