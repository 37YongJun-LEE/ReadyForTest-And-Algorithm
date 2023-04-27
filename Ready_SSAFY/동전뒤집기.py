T = int(input())
for test_case in range(1, T+1):
    data = list(input())
    temp = '0'
    cnt = 0
    for num in data:
        if temp != num:
            cnt += 1
            temp = num
    print('#{} {}'.format(test_case, cnt))