T = int(input())
for test_case in range(1, T+1):
    num = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    N = int(input())
    for i in range(1, 100):
        data = list(str(i*N))
        for j in data:
            num[j] = 1
        if sum(num.values()) == 10:
            print('#{} {}'.format(test_case, i*N))
            break