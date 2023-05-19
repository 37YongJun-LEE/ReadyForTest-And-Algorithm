# 개쓰레기 문제 : 입출력 속도가 정답을 가른다

lst = []
T = int(input())
for tc in range(T):
    lst.append(tuple(map(int, input().split())))

for tc in range(T):
    A, B, C, D = lst[tc]
    ALICE = A / B
    BOB = C / D
    print(f'#{tc + 1}', end=' ')
    if ALICE > BOB:
        print('ALICE')
    elif ALICE < BOB:
        print('BOB')
    else:
        print('DRAW')
"""

3
1 2 2 4
4 5 2 5
1 9 5 6
"""