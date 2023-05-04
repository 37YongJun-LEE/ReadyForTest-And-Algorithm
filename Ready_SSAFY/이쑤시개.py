T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    total = 0
    prev = 0

    for i in range(N):
        now = int(input())
        total += now
        if now == 0:
            total -= prev
        prev = now
    print('#{} {}'.format(test_case, total))


"""
5
10
95450
0
66012
0
95966
0
8369
4346
10639
0
5
64214
99799
0
32285
15948
1
19815
10
42094
0
90675
0
84381
58873
0
510
45755
46993
6
76475
0
83122
0
0
0
"""