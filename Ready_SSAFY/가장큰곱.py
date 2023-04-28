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
