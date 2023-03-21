import math


def solution(n, a, b):
    M = n // 2
    if (a <= M < b) or (b <= M < a):
        return math.log2(n)

    elif a <= M and b <= M:
        return solution(M, a, b)

    else:
        return solution(M, a - M, b - M)