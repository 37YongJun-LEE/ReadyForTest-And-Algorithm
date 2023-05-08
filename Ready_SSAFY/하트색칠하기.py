T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    heart = [0] * (N+1) # 0번은 빈칸 유의
    Q = int(input())
    for i in range(1, Q+1): # 0번은 빈칸이므로 띄고하기
        L, R = map(int, input().split())
        heart[L:R+1] = map(int, [i] * len(heart[L:R+1]))
    print('#{}'.format(test_case))
    for k in range(1, N+1):
        print(heart[k], end = ' ')
    print()

"""
1
9
6
5 7
7 8
4 7
7 8
8 9
4 7

"""