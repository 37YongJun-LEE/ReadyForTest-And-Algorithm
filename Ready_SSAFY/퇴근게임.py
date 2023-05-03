T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())  # N명과 부장님 번호 X
    data = list(map(int, input().split()))
    impossible = False
    start = data[0]
    m = 1
    while X != start:
        start = data[start]
        m += 1
        if m >= N:
            impossible = True
            break
    if impossible:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, m))



"""
T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())  # N명과 부장님 번호 X
    data = list(map(int, input().split()))
    
    if X not in data:
        print('#{} {}'.format(test_case, -1))
        continue
    
    impossible = False
    start = data[0]
    m = 1
    while X != start:
        start = data[start]
        m += 1
        if m >= N:
            impossible = True
            break
    if impossible:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, m))
"""