T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    triangle = []
    for i in range(N):
        triangle.append([1] * (i+1))

    for i in range(N):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    print('#{}'.format(test_case))
    for i in range(N):
        for k in triangle[i]:
            print(k, end = ' ')
        print()