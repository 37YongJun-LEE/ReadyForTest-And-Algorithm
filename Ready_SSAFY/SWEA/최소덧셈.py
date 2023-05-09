T = int(input())
for test_case in range(1, T+1):
    N = input()
    min_answer = int(N)
    for i in range(1,len(N)):
        min_answer = min(min_answer, int(N[0:i]) + int(N[i:len(N)]))
    print('#{} {}'.format(test_case, min_answer))


"""
3
1743
123
3141592
"""