T = int(input())
for test_case in range(1, T+1):
    data = list(input())

    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14

    for i in range(3, len(data)+1, 3):
        T, X, Y = data[i-3:i]


        k = int(X+Y)
        if T == 'S':
            S[k] += 1
        elif T == 'D':
            D[k] += 1
        elif T == 'H':
            H[k] += 1
        else: # C
            C[k] += 1

    S.pop(0)
    D.pop(0)
    H.pop(0)
    C.pop(0)

    error = False
    for a,b,c,d in zip(S, D, H, C):
        if a > 1 or b >1 or c > 1 or d > 1:
            error = True
    if error:
        print('#{} {}'.format(test_case, 'ERROR'))
        continue

    else:
        print('#{} {} {} {} {}'.format(test_case, 13-sum(S), 13-sum(D), 13-sum(H), 13-sum(C)))
