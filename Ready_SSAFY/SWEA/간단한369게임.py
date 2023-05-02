
N = int(input())

for i in range(1,N+1):
    cnt = 0
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end = '')
    else:
        print(i, end = '')
    print(' ', end = '')