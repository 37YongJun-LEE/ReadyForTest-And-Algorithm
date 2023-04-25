T = int(input())
for test_case in range(1, T + 1):
    data = list(input())
    cnt = 1
    answer = ''
    for s in data:
        if s.isnumeric(): cnt = int(s)
        else:
            answer += s * cnt
            cnt = 1
    print('#{} {}'.format(test_case, answer))
