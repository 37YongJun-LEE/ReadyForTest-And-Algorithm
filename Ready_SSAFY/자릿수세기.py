T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    length = len(str(N))
    answer = 0
    for i in range(1, length):
        answer +=  i * ((10 ** i) - (10 ** (i-1)))
    answer += (N - 10 ** (length-1) + 1) * length
    print(answer)