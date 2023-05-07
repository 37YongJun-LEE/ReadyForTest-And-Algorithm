T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    answer = []
    for i in range(N):
        word = input()
        num = ''
        prev = ''
        for s in word:
            if s.isnumeric():
                num += s
                prev = s
            elif prev.isnumeric() and not s.isnumeric():
                answer.append(int(num))
                num = ''
                prev = s
        if num: answer.append(int(num))
    answer.sort()
    print('#{}'.format(test_case))
    for k in answer: print(k, end = ' ')
    print()
